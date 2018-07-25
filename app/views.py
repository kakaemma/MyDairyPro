from flask import jsonify, request, render_template
from app.models import DiaryModel
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
    if 'name' in request.json and 'desc' in request.json:
        if request.json['name'] and request.json['desc']:
            diary = DiaryModel(request.json['name'], request.json['desc'])
            new_diary = diary.create_diary()
            if new_diary !=None:
                return message_to_return(409, 'Diary')
            return message_to_return(201, 'Diary')

    return message_to_return(400)


@app.route('/api/<version>/entries', methods=['GET'])
def get_entries(version):
    entries = DiaryModel.get_entries()
    if entries == None:
        return message_to_return(404, 'Diaries')
    return message_to_return(200,entries)

def 





def message_to_return(status_code, optional_msg = None):
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
            'Error': 'Missing or bad parameter submitted',
        }), 400
        return response

    if status_code == 404:
        response = jsonify({

            'Error': optional_msg + ' not found',
        }), 404
        return response

