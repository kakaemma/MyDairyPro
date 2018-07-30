import unittest
from flask import json
from config import application_config
from app.models import DiaryModel
from app.views import app
from database import DatabaseConnection

class BaseClass(unittest.TestCase):
    def setUp(self):
        app.config.from_object(application_config['TestingEnv'])
        db = DatabaseConnection()
        db.create_tables()
        self.client = app.test_client()



        self.empty_diary = json.dumps({
            'name':'',
            'desc': ''
        })
        self.new_diary = json.dumps({
            'name':'Uganda rally 2018',
            'desc': 'Win all rallies'
        })
        self.edit_diary = json.dumps({
            'name':'World class developer',
            'desc': 'Attend boot camp'
        })
        self.empty_reg = json.dumps({
            'name': '',
            'email': '',
            'password': ''
        })
        self.invalid_email = json.dumps({
            'name': 'Kakaire',
            'email': 'kakaemma',
            'password': '123456'
        })
        self.short_password = json.dumps({
            'name': 'Kakaire',
            'email': 'kakaemma@gmail.com',
            'password': '1234'
        })
        self.user = json.dumps({
            'name': 'Kakaire',
            'email': 'kakaemma@gmail.com',
            'password': '1234567'
        })
        self.new_user = json.dumps({
            'name': 'Kakaire',
            'email': 'kakaemma1@gmail.com',
            'password': '1234567'
        })
        self.empty_login = json.dumps({
            'email':'',
            'password':''
        })
    def tearDown(self):
        DiaryModel.diary = []