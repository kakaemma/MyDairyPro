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
    request.get_json(force=True)
    if 'name' in request.json and 'email' in request.json \
            and 'password' in request.json:
        if request.json['name'] and request.json['email'] \
                and request.json['password']:
            user= UserModel(request.json['name'],request.json['email'],
                            request.json['email'])
            register_user = user.add_user()
            if register_user == None:
                response = jsonify({
                    'Email': request.json['email'],
                    'Status': 'successfully registered'
                }),201
                return response
            response = jsonify({
                'Conflict': 'User already exists'
            }),409
            return response
        
        response = jsonify({
            'status': 'Empty values submitted'
        }),400
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

