from validate_email import validate_email
from flask import jsonify, request, render_template
from app.models import DiaryModel,UserModel
from app import create_app


app = create_app('DevelopmentEnv')


@app.route('/')
def index():
    """
    Index route
    :return: 
    """

    return "<h2>Welcome to My Diary</h2>"


@app.route('/api/<version>/entries', methods=['POST'])
def add_entries(version):
    """
    This endpoint add an entry 
    :param version: 
    :return: 
    """
    if version == 'v1':
        request.get_json(force=True)
        if 'name' in request.json and 'desc' in request.json:
            if request.json['name'] and request.json['desc']:
                diary = DiaryModel(request.json['name'], request.json['desc'])
                new_diary = diary.create_diary()
                if new_diary is not None:
                    return message_to_return(409, 'Diary')
                return message_to_return(201, 'Diary')

        return message_to_return(400)
    return invalid_arguments()


@app.route('/api/<version>/entries', methods=['GET'])
def get_entries(version):
    """
    This entry gets a all entries
    :param version: 
    :return: 
    """
    if version == 'v1':
        entries = DiaryModel.get_entries()
        if entries is True:
            return message_to_return(404, 'Diaries')
        return message_to_return(200, entries)
    return invalid_arguments()


@app.route('/api/<version>/entries/<int:diary_id>', methods=['GET'])
def get_entry(version, diary_id):
    """
    This endpoint gets a single entry
    :param version: 
    :param diary_id: 
    :return: 
    """
    if version == 'v1' and isinstance(diary_id, int):
        entry = DiaryModel.get_entry(diary_id)
        if entry == []:
            return message_to_return(404, 'Entry')

    return invalid_arguments()


@app.route('/api/<version>/entries/<int:diary_id>', methods=['PUT'])
def modify_entry(version, diary_id):
    """
    This endpoint modifies an entry
    :param version: 
    :param diary_id: 
    :return: 
    """
    if version == 'v1' and isinstance(diary_id, int):
        request.get_json(force=True)
        if 'name' in request.json and 'desc' in request.json:
            if request.json['name'] and request.json['desc']:

                edit_entry = DiaryModel.modify_entry(diary_id,
                                                     request.json['name'],
                                                     request.json['desc'])
                if edit_entry is None:
                    return message_to_return(404, 'Diary or Entry')
                if edit_entry == 'same name':
                    return message_to_return(409, 'name')
                if edit_entry == 'modified':
                    return message_to_return(200, 'successfully modified')

        return message_to_return(400)
    return invalid_arguments()

@app.route('/api/<version>/auth/signup', methods=['POST'])
def sign_up_user(version):
    """
    This end point registers a user
    :param version: 
    :return: user added and status code 201 on success
    """
    request.get_json(force=True)
    if 'name' in request.json and 'email' in \
            request.json and 'password' in request.json:

        name =request.json['name']
        email = request.json['email']
        password = request.json['password']

        if name and email  and password:
            if not validate_email(email):
                return message_to_return(422, "Invalid Email address")
            if not len(name) >=3:
                return message_to_return(422, "Name too short")
            if not len(password) >=6:
                return message_to_return(422, "password too short. Minimum is 6")

            new_user = UserModel()
            check_user = UserModel.check_if_user_exists_using_email(email)
            if check_user:
                return jsonify({
                    "Conflict": "User already exists"
                }), 409
            new_user.register_user(name ,email,password)
            return message_to_return(201, request.json['email'])
        return message_to_return(422, "Missing values")

    return invalid_arguments()


@app.route('/api/<version>/auth/login', methods=['POST'])
def login(version):
    request.get_json(force=True)
    if 'email' in request.json and 'password' in request.json:
        email = request.json['email']
        password = request.json['password']
        if email and password:
            login = UserModel.check_if_is_valid_user(email, password)
            if login:
                return jsonify({
                    'status': "Login successful",
                    "token": "token"

                }), 200
            return invalid_user()
        return message_to_return(400)
    return invalid_arguments()

def message_to_return(status_code, optional_msg=None):
    """
    This method returns messages depending oon the status code
    :param status_code: 
    :param optional_msg: 
    :return: 
    """
    if status_code == 201:
        response = jsonify({
            'Status': optional_msg + ' successfully added'
        }), 201
        return response
    if status_code == 200:
        response = jsonify({
            'Diary entries': optional_msg
        }), 200
        return response
    if status_code == 409:
        response = jsonify({
            'Conflict': optional_msg + ' already exists'
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
            'Error': 'Missing or bad parameter submitted',
        }), 400
        return response

    if status_code == 404:
        response = jsonify({

            'Error': optional_msg + ' not found. Add entries first',
        }), 404
        return response

def invalid_arguments():
    return jsonify({
        'Error': 'Invalid parameters'
    }), 400

def invalid_user():
    return jsonify({
        'Error': 'Invalid user'
    }), 401