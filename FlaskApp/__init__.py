from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from logging.handlers import RotatingFileHandler
from flask_moment import Moment
import os
import logging
import jsonify
import requests
import pickle
import numpy as np
import sys
import os
import sklearn
from sklearn.preprocessing import StandardScaler



app = Flask(__name__)
app.config.from_object(Config)



db= SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'your email',
    "MAIL_PASSWORD": 'your password'
}

app.config.update(mail_settings)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'login'


from FlaskApp import routes, models





if __name__ == "__main__":
    app.run()
