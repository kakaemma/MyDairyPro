import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from app.models import UserModel
logged_in_user = None
def get_token():
    try:
        token = request.headers.get('Authorization')
        return token
    except Exception as exc:
        return exc

def select_method_to_return(function, *args, **kwargs):
    try:
        if len(args) == 0:
            return function()
        else:
            return function(*args, **kwargs)

    except Exception as exc:
        return exc

def validate_content_type(function):
    @wraps()
    def decorated_method(*args, **kwargs):
        if request.header.get('content-type') != 'application/json':
            response = jsonify({
                'Error': 'Content-Type not specified as application/json'
            }),400
            return response
        return select_method_to_return()
    return decorated_method

def generate_token(user_id):
    try:
        payload = {
            "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            "iat":datetime.datetime.utcnow(),
            "sub":user_id
            }
        auth_token = jwt.encode( payload,'TEAM TIA', algorithm='HS256' )
        return auth_token
    except Exception as exc:
        return exc

def decode_token(token):
    try:
        payload = jwt.decode(token, 'TEAM TIA')
        user = payload['sub']
        return user

    except jwt.ExpiredSignature:
        response = jsonify({'Error': 'Token expired please login again'})
        response.status_code = 401
        return response

    except jwt.InvalidTokenError:
        response = jsonify({'Error':  'Invalid token'})
        response.status_code = 401
        return response

def validate_token(function):
    @wraps()
    def decorated_method(function, *args, **kwargs):
        token = get_token()
        if token is None:
            return jsonify({
                "Error": "There is no token in the header"
            }),401
        try:
            user_id = decode_token(token)
            search_for_user_with_id = UserModel.get_user_by_id(user_id)
            if search_for_user_with_id is None:
                return jsonify({
                    'Error': 'Mismatching or wrong token'
                }),401
            logged_in_user = user_id
        except Exception as exc:
            return exc

        return select_method_to_return(function, *args, **kwargs)
    return decorated_method
