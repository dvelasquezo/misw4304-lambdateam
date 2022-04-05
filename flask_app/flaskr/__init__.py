from flask import Flask
from .instance.config import app_config
from flask_restful import Api
from .modelos import db
from .vistas import VistaRoot, VistaBlacklists

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('instance/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = app.app_context()
    app_context.push()
    db.init_app(app)
    db.create_all()
    api = Api(app)
    api.add_resource(VistaRoot, '/')
    api.add_resource(VistaBlacklists, '/blacklists')
    return app
