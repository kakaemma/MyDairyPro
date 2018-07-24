from flask import jsonify, request, render_template
from app import create_app


app = create_app('TestingEnv')


@app.route('/')
def index():
    """
    Index route
    :return: 
    """

    return "<h2>Welcome to MyDiary</h2>"


@app.route('/api/<version>/register', methods=['POST'])
def register(version):
    """
    This end point registers a user
    :param version: 
    :return: 
    """
    user_data = request.json
    if 'name' in user_data and 'email' in user_data and 'password' in user_data:
        pass



@app.route('/api/<version>/register', methods=['POST'])
def register(version):
    """
    This end point signs in a user
    :param version: 
    :return: 
    """
    pass

