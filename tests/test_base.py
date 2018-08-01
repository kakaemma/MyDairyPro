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
            'email': 'kakazzzzzz@gmail.com',
            'password': '1234567'
        })
        self.new_user_with_ivalid_param = json.dumps({
            'name': 'Kakaire',
            'emadil': 'kakazzzzzz@gmail.com',
            'password': '1234567'
        })
        self.empty_login = json.dumps({
            'email':'',
            'password':''
        })
        self.invalid_user = json.dumps({
            'email':'wrong@kk.cc',
            'password':'123456'
        })
        self.valid_user = json.dumps({
            'email': 'kakaemma@gmail.com',
            'password': '1234567'
        })
        self.params = json.dumps({
            'emasil': 'kakaemma@gmail.com',
            'password': '1234567'
        })
        self.empty_diary = json.dumps({
            'name': ''
        })
        self.new_diary = json.dumps({
            'name': 'Uganda rally 2018',
            'desc': 'wining rally'
        })
        self.new_diary_2 = json.dumps({
            'name': 'Uganda rally 2018',
            'desc': 'wining rally'
        })
        self.edit_diary = json.dumps({
            'name': 'Pearl rally 2018',
            'desc': 'Winn pearl'
        })
        self.empty_desc = json.dumps({
            'desc': ''
        })
        self.short_desc = json.dumps({
            'desc': 'Andela'
        })
        self.desc = json.dumps({
            'desc': 'Andela Uganda cohort 10 boot camp'
        })
        self.desc2 = json.dumps({
            'desc': 'Andela Uganda cohort 10 boot camp week one'
        })

    def tearDown(self):
        db = DatabaseConnection()
        db.drop_table('users')
        db.drop_table('entries')
