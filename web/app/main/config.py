import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    PYTHONUNBUFFERED = 1


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'sample'
    BASIC_AUTH_PASSWORD = 'pass'
    BASIC_AUTH_REALM = 'Basic Auth Required'
    MONGODB_USERNAME = os.environ['MONGODB_USERNAME']
    MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']
    MONGODB_HOSTNAME = os.environ['MONGODB_HOSTNAME']
    MONGODB_DATABASE = os.environ['MONGODB_DATABASE']
    MONGO_URI = ('mongodb://' + MONGODB_USERNAME + ':' +
                MONGODB_PASSWORD + '@' + MONGODB_HOSTNAME + ':27017/' +
                MONGODB_DATABASE + '?authSource=admin')
    MONGODB_SETTINGS = {
        'db' : os.environ['MONGODB_DATABASE'],
        'host'  : ('mongodb://' + os.environ['MONGODB_USERNAME'] + ':' +
                    os.environ['MONGODB_PASSWORD'] + '@' +
                    os.environ['MONGODB_HOSTNAME'] + ':27017/' +
                    os.environ['MONGODB_DATABASE'] + '?authSource=admin'),
    }


class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'sample'
    BASIC_AUTH_PASSWORD = 'pass'
    BASIC_AUTH_REALM = 'Basic Auth Required'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    BASIC_AUTH_USERNAME = 'sample'
    BASIC_AUTH_PASSWORD = 'pass'
    BASIC_AUTH_REALM = 'Basic Auth Required'


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
