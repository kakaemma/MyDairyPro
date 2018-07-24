from flask import jsonify, request, render_template
from app.models import UserModel
from app import create_app


app = create_app('TestingEnv')


@app.route('/')
def index():
    """
    Index route
    :return: 
    """

    return "<h2>Welcome to My Diary</h2>"


@app.route('/api/<version>/register', methods=['POST'])
def register(version):
    """
    This end point registers a user
    :param version: 
    :return: 
    """
    user_data = request.json
    if 'name' in user_data and 'email' in user_data \
            and 'password' in user_data:
        user= UserModel(user_data['name'],
                        user_data['email', user_data['password']])
        register_user = user.add_user()
        if register_user == None:
            response = jsonify({
                'Email': user_data['email'],
                'Status': 'successfully registered'
            }),201
            return response
        response = jsonify({
            'Email': user_data['email'],
            'Conflict': 'User already exists'
        }),409
        return response
    response = jsonify({
        'Error': 'Missing or bad parameter submitted',
    }),400
    return response


@app.route('/api/<version>/login', methods=['POST'])
def login(version):
    """
    This end point signs in a user
    :param version: 
    :return: 
    """
    pass

