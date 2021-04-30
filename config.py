import os
from datetime import timedelta

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI  = 'mysql://MASTER_USERNAME:PASSWORD@ENDPOINT:PORT#/healthai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
    UPLOAD_PATH = 'uploads'
