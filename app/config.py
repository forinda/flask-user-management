import os
from secrets import token_hex

class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = token_hex(20)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_ADMIN = 'forinda82@gmail.com'

class ProductionConfig(object):
    DEBUG = False
    SECRET_KEY = token_hex(40)