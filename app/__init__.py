import os
from flask_api import FlaskAPI
from config import application_config


def create_app(config_name):
    app = FlaskAPI(__name__)
    APP_ROOT = os.path.dirname(app.instance_path)
    app.config.from_object(application_config[config_name])
    app.config.from_pyfile(APP_ROOT+'/config.py')

    return app
