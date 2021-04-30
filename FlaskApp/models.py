from FlaskApp import db, login, app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
import jwt
from hashlib import md5
from datetime import datetime

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    ssn_hash = db.Column(db.String(128))
    phone = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    db_day = db.Column(db.Integer)
    db_month = db.Column(db.Integer)
    db_year = db.Column(db.Integer)
    bp = db.Column(db.String(64))
    diabetes = db.Column(db.String(64))
    smoke = db.Column(db.String(64))
    terms = db.Column(db.Boolean(), default=False)
    privacy = db.Column(db.Boolean(), default=False)
    consent = db.Column(db.Boolean(), default=False)

    #additional profile information below
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_ssn_hash(self, ssn):
        self.ssn_hash = generate_password_hash(ssn)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Pneumonia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prediction = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class HeartDiseasePrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    Age= db.Column(db.Integer)
    Gender= db.Column(db.Integer)
    ChestPain= db.Column(db.Integer)
    BloodPressure= db.Column(db.Integer)
    ElectrocardiographicResults= db.Column(db.Integer)
    MaxHeartRate= db.Column(db.Integer)
    ExerciseInducedAngina= db.Column(db.Integer)
    STdepression= db.Column(db.Float(precision=9))
    MajorVesselsNo= db.Column(db.Integer)
    Thalassemia=db.Column(db.Integer)
    prediction= db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Heart Disease {}>'.format(self.prediction)


class BreastCancer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    texture_mean = db.Column(db.Float(precision=9))
    perimeter_mean = db.Column(db.Float(precision=9))
    smoothness_mean = db.Column(db.Float(precision=9))
    compactness_mean = db.Column(db.Float(precision=9))
    concavity_mean = db.Column(db.Float(precision=9))
    concave_points_mean = db.Column(db.Float(precision=9))
    symmetry_mean = db.Column(db.Float(precision=9))
    radius_se = db.Column(db.Float(precision=9))
    compactness_se = db.Column(db.Float(precision=9))
    concavity_se = db.Column(db.Float(precision=9))
    concave_points_se = db.Column(db.Float(precision=9))
    texture_worst = db.Column(db.Float(precision=9))
    smoothness_worst = db.Column(db.Float(precision=9))
    compactness_worst = db.Column(db.Float(precision=9))
    concavity_worst = db.Column(db.Float(precision=9))
    concave_points_worst = db.Column(db.Float(precision=9))
    symmetry_worst = db.Column(db.Float(precision=9))
    fractal_dimension_worst = db.Column(db.Float(precision=9))
    prediction= db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Breast Cancer {}>'.format(self.Prediction)

class LiverDisease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    Gender = db.Column(db.Integer)
    Total_Bilirubin = db.Column(db.Float(precision=9))
    Direct_Bilirubin = db.Column(db.Float(precision=9))
    Alkaline_Phosphotase =db.Column(db.Integer)
    Alamine_Aminotransferase = db.Column(db.Integer)
    Aspartate_Aminotransferase = db.Column(db.Integer)
    Total_Protiens = db.Column(db.String(128))
    Albumin = db.Column(db.String(128))
    Albumin_and_Globulin_Ratio = db.Column(db.String(128))
    prediction= db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class GeneralDisease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    Symptom1 = db.Column(db.String(128))
    Symptom2 = db.Column(db.String(128))
    Symptom3 = db.Column(db.String(128))
    Symptom4 = db.Column(db.String(128))
    Symptom5 = db.Column(db.String(128))
    prediction= db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
