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
    except Exception as ex:
        return ex

def select_method_to_return(function, *args, **kwargs):
    try:
        if len(args) == 0 and len(kwargs)==0:
            return function()
        else:
            return function(*args, **kwargs)

    except Exception as exc:
        return jsonify({
            "Failed with exception":exc
        })

def validate_content_type(func):

    @wraps(func)
    def decorated_method(*args, **kwargs):
        if request.headers.get('content-type') != 'application/json':
            return jsonify({
                'Error': 'Content-Type not specified as application/json'
            }), 400
        return select_method_to_return(func, *args, **kwargs)
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
        return jsonify({'Error': 'Token expired please login again'}),401


    except jwt.InvalidTokenError:
        return jsonify({'Error':  'Invalid token'}),401

def validate_token(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = get_token()
        if token is None:
            return jsonify(
                {
                    'Error': 'There is no token'
                }), 401
        try:
            user_id = decode_token(token)
            result = UserModel.get_user_by_id(user_id)
            if result is None:
                return jsonify({
                    'Error': 'Mismatching or wrong token'
                }),401

        except Exception as ex:
            return jsonify({
                'Failed with exception': ex
            }), 500

        return select_method_to_return(func, *args, **kwargs)
    return decorated_function