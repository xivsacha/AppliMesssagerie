import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-tres-difficile'
    SQLALCHEMY_DATABASE_URI = 'mysql://flaskuser:password@10.57.33.9/appli_messagerie'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
