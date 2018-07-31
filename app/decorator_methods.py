import jwt
from datetime import datetime
from functools import wraps
from flask import request, jsonify


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


