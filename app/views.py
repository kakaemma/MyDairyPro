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
    pass

