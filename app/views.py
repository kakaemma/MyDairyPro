from flask import jsonify, request
from app import create_app


app = create_app('TestingEnv')


@app.route('/')
def index():
    """
    Index route
    :return: 
    """

    return "<h2>Welcome to My Diary</h2>"


@app.route('/api/<version>/entries', methods=['POST'])
def add_entries(version):
    request.get_json(force=True)
    if 'name' in request.json and 'description' in request.json:
        pass
    return message_to_return(400)







def message_to_return(status_code, optional_msg = None):
    if status_code == 201:
        response = jsonify({
            'Status': request.json['email'] + \
                      ' successfully registered'
        }), 201
        return response
    if status_code == 409:
        response = jsonify({
            'Conflict': optional_msg +' already exists'
        }), 409
        return response

    if status_code == 422:
        response = jsonify({
            'Error': 'Unprocessable entity',
            'msg': optional_msg
        }), 422
        return response

    if status_code == 400:
        response = jsonify({
            ''
            'Error': 'Missing or bad parameter submitted',
        }), 400
        return response
