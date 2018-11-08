class Config(object):
    SERVER_NAME = '127.0.0.1:5000'
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False

class TestConfig(Config):
    SERVER_NAME = '127.0.0.1:5050'
    DEBUG = True
    TESTING = True
    JSON_AS_ASCII = False

DB_NAME = "pigeon"
DB_USER = "pigeon"
DB_PASS = "pigeon"
DB_HOST = "127.0.0.1"