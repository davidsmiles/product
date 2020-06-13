import os


class BaseConfig():
    ENV = 'development'
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = 'microservice'
    SEND_FILE_MAX_AGE_DEFAULT = 0


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    MONGODB_SETTINGS = {
        'host': os.environ.get("PROD_DATABASE_URL", "mongodb://localhost:27017/app-testing")
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGODB_SETTINGS = {
        'host': os.environ.get("PROD_DATABASE_URL", "mongodb://david:secret@database/webshop")
    }


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
