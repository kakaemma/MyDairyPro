import unittest
from flask import json
from instance.config import application_config
from app.views import app

class BaseClass(unittest.TestCase):
    def setUp(self):
        app.config.from_object(application_config['TestingEnv'])
        self.client = app.test_client()

        self.empty_reg = json.dumps({
            'name': '',
            'emaicl': '',
            'password': ''
        })

        self.invalid_email = json.dumps({
            'name': 'Emmanuel',
            'email': 'kakaemma',
            'password': '123456'
        })