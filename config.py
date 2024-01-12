import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-tres-difficile'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskuser:password@192.168.70.249/appli_messagerie'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
