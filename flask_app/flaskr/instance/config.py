from os import environ


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:Lambdateam+@db-listas-negras.cwny75wezfae.us-east-1.rds.amazonaws.com:5432/db_listas_negras"
    PROPAGATE_EXCEPTIONS = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:localhost:5432/db_listas_negras'
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
}
