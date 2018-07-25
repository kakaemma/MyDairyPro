from flask import jsonify, request, render_template
from app.models import UserModel, DiaryModel
from validate_email import validate_email
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
    """ This end point registers a user
    :param version: 
    :return: 
    """
    request.get_json(force=True)
    if 'name' in request.json and 'email' in request.json \
            and 'password' in request.json:
        if request.json['name'] and request.json['email'] \
                and request.json['password']:

            if len(request.json['password']) < 6:
                return message_to_return(422, 'Password too short')

            if validate_email(request.json['email']):
                user = UserModel(request.json['name'],
                                 request.json['email'], request.json['email'])

                register_user = user.add_user()
                print(register_user)
                if register_user == None:
                    return  message_to_return(201, request.json['email'])
                return message_to_return(409, 'email')
            return message_to_return(422)
    return message_to_return(400)


@app.route('/api/<version>/entries', methods=['POST'])
def add_entries(version):
    request.get_json(force=True)
    if 'name' in request.json and 'desc' in request.json:
        if request.json['name'] and request.json['desc']:
            diary = DiaryModel(request.json['name'], request.json['desc'])
            new_diary = diary.create_diary()
            if new_diary !=None:
                return message_to_return(409, 'Diary')
            return message_to_return(201, 'Diary')

    return message_to_return(400)




def message_to_return(status_code, optional_msg = None):
    if status_code == 201:
        response = jsonify({
            'Status': optional_msg + ' successfully added'
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
