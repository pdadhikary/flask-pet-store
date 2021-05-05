class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ""
    SESSION_COOKIE_SECURE = True
    USER_UNAUTHORIZED_ENDPOINT = ""


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///pet_store.db"
    SECRET_KEY = "62fe21021befc0e49fb41bd4e3f10d887c3bfd87f9a0d425"
    SESSION_COOKIE_SECURE = False
