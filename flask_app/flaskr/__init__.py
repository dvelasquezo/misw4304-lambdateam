from email.mime import application
from flask import Flask
from .instance.config import app_config
from flask_restful import Api
from .modelos import db
from .vistas import VistaRoot, VistaBlacklistsPost, VistaBlacklistsGet

def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(app_config[config_name])
    application.config.from_pyfile('instance/config.py')
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = application.app_context()
    app_context.push()
    db.init_app(application)
    db.create_all()
    api = Api(application)
    api.add_resource(VistaRoot, '/')
    api.add_resource(VistaBlacklistsPost, '/blacklists')
    api.add_resource(VistaBlacklistsGet, '/blacklists/<string:email>')

    return application
