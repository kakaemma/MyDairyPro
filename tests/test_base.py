import unittest
from flask import json
from config import application_config
from app.models import UserModel
from app.views import app

class BaseClass(unittest.TestCase):
    def setUp(self):
        app.config.from_object(application_config['TestingEnv'])
        self.client = app.test_client()

        self.empty_reg = json.dumps({
            'name': '',
            'email': '',
            'password': ''
        })

        self.invalid_email = json.dumps({
            'name': 'Emmanuel',
            'email': 'kakaemma',
            'password': '123456'
        })
        self.short_password = json.dumps({
            'name': 'Kakaire',
            'email': 'kakaemma@gmail.com',
            'password': '1234'
        })
        self.user = json.dumps({
            'name': 'Emmanuel',
            'email': 'kakaemma@gmail.com',
            'password': '1234567'
        })
    def tearDown(self):
        UserModel.users = []