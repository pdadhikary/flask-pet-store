import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ""
    SESSION_COOKIE_SECURE = True
    USER_UNAUTHORIZED_ENDPOINT = ""


class ProductionConfig(Config):
    ENV = 'production'
    pass


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///pet_store.db"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_SECURE = False
