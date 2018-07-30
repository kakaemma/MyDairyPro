import unittest
from flask import json
from config import application_config
from app.models import DiaryModel
from app.views import app

class BaseClass(unittest.TestCase):
    def setUp(self):
        app.config.from_object(application_config['TestingEnv'])
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
    def tearDown(self):
        DiaryModel.diary = []