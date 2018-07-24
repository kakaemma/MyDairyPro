from app.views import app
from flask_testing import TestCase
import unittest


class TestDevelopmentEnvironment(TestCase):
    """ Test app in development environment"""
    def create_app(self):
        app.config.from_object('instance.config.DevelopmentEnvironment')
        return app

    def test_app_in_development_env(self):
        """ Should return debug is true if debug is enabled"""
        self.assertTrue(app.config['DEBUG'])