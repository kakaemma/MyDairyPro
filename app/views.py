from validate_email import validate_email
from flask_cors import CORS
from flask import jsonify, request, render_template
from app.models import DiaryModel,UserModel
from app import create_app
from app.decorator_methods import generate_token, decode_token,get_token
from app.decorator_methods import validate_content_type,validate_token


app = create_app('DevelopmentEnv')
cors = CORS(app)





@app.route('/')
def index():
    """
    Index route
    :return: 
    """

    return render_template('index.html')


@app.route('/api/<version>/entries', methods=['POST'])
@validate_token
@validate_content_type
def add_entries(version):
    """
    This endpoint add an entry 
    :param version: 
    :return: 
    """
    if version == 'v1':
        request.get_json(force=True)
        token =get_token()
        user_id =decode_token(token)
        if 'name' in request.json and 'desc' in request.json :
            name = request.json['name']
            desc = request.json['desc']
            if name and desc and desc:

                diary = DiaryModel(name, desc, user_id)
                new_diary = diary.create_diary()
                if new_diary is True:
                    return message_to_return(409, 'Diary')
                return jsonify({
                    "Status": "Diary successfully added",
                    "Entry": new_diary
                }), 201

        return message_to_return(400)
    return invalid_arguments()


@app.route('/api/<version>/entries', methods=['GET'])
@validate_token
def get_entries(version):
    """
    This entry gets a all entries
    :param version: 
    :return: 
    """
    if version == 'v1':
        token = get_token()
        user_id = decode_token(token)
        print(user_id)
        entries = DiaryModel.get_entries(str(user_id))
        if entries is False:
            return message_to_return(404, 'Diaries')
        return message_to_return(200, entries)
    return invalid_arguments()


@app.route('/api/<version>/entries/<int:diary_id>', methods=['GET'])
@validate_token
def get_entry(version, diary_id):
    """
    This endpoint gets a single entry
    :param version: 
    :param diary_id: 
    :return: 
    """
    if version == 'v1':
        token = get_token()
        user_id = decode_token(token)
        print(user_id)
        entry = DiaryModel.get_entry(diary_id, user_id)
        if entry is False:
            return message_to_return(404, 'Entry')
        return message_to_return(200, entry)

    return invalid_arguments()


@app.route('/api/<version>/entries/<int:diary_id>', methods=['PUT'])
@validate_token
@validate_content_type
def modify_entry(version, diary_id):
    """
    This endpoint modifies an entry
    :param version: 
    :param diary_id: 
    :return: 
    """
    if version == 'v1':
        request.get_json(force=True)
        token = get_token()
        user_id = decode_token(token)
        if 'name' in request.json and 'desc' in request.json:
            name = request.json['name']
            desc = request.json['desc']
            if name and desc:

                edit_entry = DiaryModel.modify_entry(diary_id,
                                                     request.json['name'],
                                                     request.json['desc'],
                                                     user_id)
                print(edit_entry)
                if edit_entry is False:
                    return message_to_return(404, 'Diary or Entry')
                if edit_entry == 'update with same name':
                    return message_to_return(409, 'name')
                if edit_entry == 1:
                    return message_to_return(200, 'successfully modified')

        return message_to_return(400)
    return invalid_arguments()


@app.route('/api/<version>/auth/signup', methods=['POST'])
@validate_content_type
def sign_up_user(version):
    """
    This end point registers a user
    :param version: 
    :return: user added and status code 201 on success
    """
    request.get_json(force=True)
    if 'name' in request.json and type(request.json['name']) is str\
            and 'email' in request.json and 'password' in request.json\
            :

        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        if name and name.isalpha() and email and password:
            if not validate_email(email):
                return invalid_email()
            if not len(name) >= 3:
                return message_to_return(400, "Name too short")
            if not len(password) >= 6:
                return message_to_return(400, "password too short. Minimum is 6")

            new_user = UserModel()
            check_user = UserModel.check_if_user_exists_using_email(email)
            if check_user:
                return jsonify({
                    "Error": "User already exists"
                }), 409
            new_user.register_user(name, email, password)
            return message_to_return(201, request.json['email'])
        return message_to_return(400, "Missing values")

    return invalid_arguments()


@app.route('/api/<version>/auth/login', methods=['POST'])
@validate_content_type
def login(version):
    request.get_json(force=True)
    if 'email' in request.json and 'password' in request.json :
        email = request.json['email']
        password = request.json['password']
        if email and password:
            login_id = UserModel.check_if_is_valid_user(email, password)
            if login_id:
                return jsonify({
                    'status': "Login successful",
                    "token": generate_token(login_id[0]).decode()

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
            'Status': optional_msg,
            'message': ' successfully added'
        }), 201
        return response
    if status_code == 200:
        response = jsonify({
            'Diary entries': optional_msg
        }), 200
        return response
    if status_code == 409:
        response = jsonify({
            'Error': optional_msg + ' already exists'
        }), 409
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
        'Error': 'Invalid email or password'
    }), 401

def invalid_email():
    return jsonify({
        'Error': 'Invalid Email address'
    }), 400
@app.errorhandler(404)
def endpoint_not_found(e):
    return jsonify({
        "Error":"Please check the format of your address"
    }), 404

@app.errorhandler(405)
def endpoint_not_found(e):
    return jsonify({
        "Error":"Method not allowed"
    }), 405