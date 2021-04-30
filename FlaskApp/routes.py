from flask import render_template, flash, redirect, request, send_from_directory
from FlaskApp import app, db, login, mail
from FlaskApp.forms import LoginForm, RegistrationForm, EmptyForm, EditProfileForm, ResetPasswordForm, ResetPasswordRequestForm, BasePrediction, BreastForm, LiverPrediction, GenDiseasePrediction
from flask_login import current_user, login_user, logout_user, login_required
from FlaskApp.models import User, Post, HeartDiseasePrediction, BreastCancer, Pneumonia, LiverDisease, GeneralDisease
from werkzeug.urls import url_parse
from FlaskApp.email import send_password_reset_email, send_email
from datetime import datetime
import jsonify
import json
import requests
import pickle
import numpy as np
import pandas as pd
import sys
import os
import sklearn
from sklearn.preprocessing import StandardScaler
from os.path import join, dirname, realpath
from sklearn.ensemble import VotingClassifier
from keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import BaggingClassifier
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename
from sklearn.svm import SVC
from flask_mail import Message
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import json

# load model
from keras.models import load_model


# load model

# model_heartdisease = pickle.load(open('FlaskApp/static/heartdisease.pkl', 'rb'))
# file = join(dirname(realpath(__file__)), 'static/heartdisease4.pkl')
# f = open('FlaskApp/static/heartdisease4.pkl', 'rb')
# mydict = pickle.load(f)
# joblib_file = '/var/www/FlaskApp/FlaskApp/heart_disease_model.pkl'
# joblib_model = joblib.load(joblib_file)





@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="index")


@app.route('/about')
def about():
    return render_template('about.html', title="about")

@app.route('/partner')
def partner():
    return render_template('partner.html', title="partner")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect('/login')

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = '/index'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/user')
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.timestamp.desc())
    heart_condition = HeartDiseasePrediction.query.filter_by(user_id=current_user.id).order_by(HeartDiseasePrediction.timestamp.desc())
    breast_cancer = BreastCancer.query.filter_by(user_id=current_user.id).order_by(BreastCancer.timestamp.desc())
    pneumonia = Pneumonia.query.filter_by(user_id=current_user.id).order_by(Pneumonia.timestamp.desc())
    liver = LiverDisease.query.filter_by(user_id=current_user.id).order_by(LiverDisease.timestamp.desc())
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, hearts = heart_condition, breast_cancer = breast_cancer, pneumonia = pneumonia, liver=liver)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegistrationForm()

    if form.validate_on_submit():
        user= User(username=form.username.data, email=form.email.data, phone=form.phone.data, db_day=form.db_day.data, db_month=form.db_month.data, db_year= form.db_year.data,  first_name = form.first_name.data, last_name=form.last_name.data, bp = form.bp.data, diabetes=form.diabetes.data, smoke = form.smoke.data, terms=form.terms.data, privacy = form.privacy.data, consent=form.consent.data)
        user.set_password(form.password.data)
        user.set_ssn_hash(str(form.ssn.data))
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now are registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)



@app.route('/assessment', methods=['GET', 'POST'])
@login_required
def assessment():
    return render_template('assessment.html')

@app.route("/library")
@login_required
def library():
    data = pd.read_csv("FlaskApp/static/symptom_Description.csv")
    precaution = pd.read_csv('FlaskApp/static/symptom_precaution.csv')
    combined_data = pd.merge(data,precaution,on='Disease') #combining 2 dataframes
    combined_data = combined_data.sort_values('Disease')
    combined_data = combined_data[1:]



    jsonfiles = json.loads(combined_data.to_json(orient='records'))

    return render_template('view.html', data = jsonfiles)


@app.route('/breastcancer', methods=['GET', 'POST'])
@login_required
def breastcancer():
    form = BreastForm()
    if form.validate_on_submit():
        bagg = pickle.load(open('FlaskApp/static/breastcancer.pkl', 'rb'))
        texture_mean_data = float(form.texture_mean.data)
        fractal_dimension_worst_data = float(form.fractal_dimension_worst.data)
        perimeter_mean_data = float(form.perimeter_mean.data)
        smoothness_mean_data = float(form.smoothness_mean.data)
        compactness_mean_data =float(form.compactness_mean.data)
        concavity_mean_data=float(form.concavity_mean.data)
        concave_points_mean_data = float(form.concave_points_mean.data)
        symmetry_mean_data =float(form.symmetry_mean.data)
        radius_se_data = float(form.radius_se.data)
        compactness_se_data = float(form.compactness_se.data)
        concavity_se_data = float(form.concavity_se.data)
        concave_points_se_data = float(form.concave_points_se.data)
        texture_worst_data = float(form.texture_worst.data)
        smoothness_worst_data = float(form.smoothness_worst.data)
        compactness_worst_data = float(form.compactness_worst.data)
        concavity_worst_data = float(form.concavity_worst.data)
        concave_points_worst_data = float(form.concave_points_worst.data)
        symmetry_worst_data = float(form.symmetry_worst.data)

        prediction=bagg.predict([[texture_mean_data, perimeter_mean_data, smoothness_mean_data, compactness_mean_data, concavity_mean_data, concave_points_mean_data, symmetry_mean_data, radius_se_data, compactness_se_data, concavity_se_data, concave_points_se_data, texture_worst_data, smoothness_worst_data, compactness_worst_data, concavity_worst_data, concave_points_worst_data, symmetry_worst_data, fractal_dimension_worst_data]])
        symptoms= BreastCancer(texture_mean = texture_mean_data, perimeter_mean=perimeter_mean_data, smoothness_mean=smoothness_mean_data, compactness_mean=compactness_mean_data, concavity_mean=concavity_mean_data, concave_points_mean=concave_points_mean_data, symmetry_mean=symmetry_mean_data, radius_se=radius_se_data, compactness_se=compactness_se_data, concavity_se=concavity_se_data, concave_points_se=concavity_se_data, texture_worst=texture_worst_data, smoothness_worst=smoothness_worst_data, compactness_worst=compactness_worst_data, concavity_worst=concavity_worst_data, concave_points_worst=concave_points_worst_data, symmetry_worst=symmetry_worst_data, fractal_dimension_worst=fractal_dimension_worst_data, prediction= int(prediction), user_id=int(current_user.id))
        db.session.add(symptoms)
        db.session.commit()

        if prediction==1:
            return render_template('breastcancer.html', prediction_text="You may have breast cancer", title='Heart Disease', form= form)
        else:
            return render_template('breastcancer.html', prediction_text="Great! It appears your breast cancer is benign.", form = form, smooth_e = smoothness_worst)

    return render_template('formcancer.html', form=form)

@app.route('/symptoms', methods=['GET', 'POST'])
@login_required
def symptoms():

    df=pd.read_csv('FlaskApp/static/heart_disease.csv')
    X=df.drop(['target', 'fbs', 'chol', 'slope'], axis=1)
    y=df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    bagg = BaggingClassifier(n_estimators=100, random_state=42)
    bagg.fit(X_train, y_train)
    y_pred_bagg=bagg.predict(X_test)
    score=accuracy_score(y_test, y_pred_bagg)

    form = BasePrediction()
    if form.validate_on_submit():
        pred=bagg.predict(scaler.transform(np.array([[int(form.Age.data), int(form.Gender.data), int(form.ChestPain.data), int(form.BloodPressure.data), int(form.ElectrocardiographicResults.data), int(form.MaxHeartRate.data), int(form.ExerciseInducedAngina.data), float(form.STdepression.data), int(form.MajorVesselsNo.data), int(form.Thalassemia.data)]])))
        symptoms= HeartDiseasePrediction(Age=form.Age.data, Gender=form.Gender.data, ChestPain=form.ChestPain.data, BloodPressure=form.BloodPressure.data, ElectrocardiographicResults=form.ElectrocardiographicResults.data, MaxHeartRate= form.MaxHeartRate.data, ExerciseInducedAngina = form.ExerciseInducedAngina.data, STdepression=float(form.STdepression.data), MajorVesselsNo=form.MajorVesselsNo.data, Thalassemia = form.Thalassemia.data, prediction= int(pred), user_id=int(current_user.id))

        db.session.add(symptoms)
        db.session.commit()

        if pred==1:
            return render_template('heartdisease_prediction.html', prediction_text="You may have a heart disease", title='Heart Disease')
        else:
            return render_template('heartdisease_prediction.html', prediction_text="Great! It appears you may not have a Heart Disease.", title='Heart Disease')

    return render_template('symptom.html', form=form)


def pneumonia_predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    model_pneumonia = load_model('FlaskApp/static/pneumoniadisease.h5')
    x=image.img_to_array(img)
    x=x/255
    x=np.expand_dims(x, axis=0)
    preds = model_pneumonia.predict(x)
    return preds

@app.route('/pneumoniadisease', methods=['GET', 'POST'])
@login_required
def pneumoniadisease():
    if request.method=="GET":
        return render_template('pneumoniadisease.html', title='Pneumonia Disease')
    else:
        f=request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,'uploads',  secure_filename(f.filename))
        f.save(file_path)

        prediction = pneumonia_predict(file_path)
        pred=np.argmax(prediction, axis=1)
        symptoms = Pneumonia(prediction=pred[0], user_id=int(current_user.id))

        db.session.add(symptoms)
        db.session.commit()
        if pred[0]==1:
            return render_template('pneumonia_prediction.html', prediction_text="This Chest X-Ray shows an area of lung inflammation indicating the presence of Pneumonia. Please consult a doctor for a diagnosis", file_name = f.filename, title='Pneumonia Disease')
        else:
            return render_template('pneumonia_prediction.html', prediction_text="Great! It appears you don't have Pneumonia.", file_name= f.filename, title='Pneumonia Disease')


@app.route('/liverdisease', methods=['GET','POST'])
@login_required
def liverdisease():
    model_liverdisease = pickle.load(open('FlaskApp/static/liverdisease.pkl', 'rb'))
    form = LiverPrediction()
    if form.validate_on_submit():
        Age=int(form.Age.data)
        Gender=int(form.Gender.data)
        Total_Bilirubin= float(form.Total_Bilirubin.data)
        Direct_Bilirubin= float(form.Direct_Bilirubin.data)
        Alkaline_Phosphotase= int(form.Alkaline_Phosphotase.data)
        Alamine_Aminotransferase= int(form.Alamine_Aminotransferase.data)
        Aspartate_Aminotransferase= int(form.Aspartate_Aminotransferase.data)
        Total_Protiens= float(form.Total_Protiens.data)
        Albumin= float(form.Albumin.data)
        Albumin_and_Globulin_Ratio= float(form.Albumin_and_Globulin_Ratio.data)
        pred=model_liverdisease.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])


        symptoms = LiverDisease(Age = int(form.Age.data), Gender = int(form.Gender.data), Total_Bilirubin =float(form.Total_Bilirubin.data), Direct_Bilirubin = float(form.Direct_Bilirubin.data), Alkaline_Phosphotase = int(form.Alkaline_Phosphotase.data), Alamine_Aminotransferase = int(form.Alamine_Aminotransferase.data), Aspartate_Aminotransferase = int(form.Aspartate_Aminotransferase.data), Total_Protiens = float(form.Total_Protiens.data), Albumin = float(form.Albumin.data), Albumin_and_Globulin_Ratio = float(form.Albumin_and_Globulin_Ratio.data), prediction = pred[0],user_id=int(current_user.id))
        db.session.add(symptoms)
        db.session.commit()
        if int(pred[0])==1:
            return render_template('liverdisease_prediction.html', prediction_text="Oops! You seem to have Liver Disease.", title='Liver Disease')
        else:
            return render_template('liverdisease_prediction.html', prediction_text="Great! You don't seem to be showing any signs of Liver Disease.", title='Liver Disease')
    else:
        return render_template('liverdisease.html', title='Liver Disease', form=form)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory('uploads', filename)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()



@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():

    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect('/edit_profile')
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect('/index')
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect('login')
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect('/index')
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect('/index')
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect('/login')
    return render_template('reset_password.html', form=form)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('term.html')


@app.route('/generaldisease', methods=['GET', 'POST'])
@login_required
def generaldisease():

    model = pickle.load(open('FlaskApp/static/diseasepred_symptoms.pkl', 'rb'))

    form = GenDiseasePrediction()
    if form.validate_on_submit():
        from_form = request.form['Symptom1']


        count_vect = CountVectorizer()
        tfidf_transformer = TfidfTransformer()


        count_vect_data = count_vect.transform([from_form])
        tfidf_transformer_data = tfidf_transformer.transform(count_vect_data)
        prediction = model.predict(tfidf_transformer_data)
        prediction_name = prediction_map.get(str(prediction[0]))

        response = {
            'status': 200,
            'prediction':prediction_name,
            'created_at': datetime.datetime.now()
        }
        output = jsonify(response)
        return render_template('generalDiseasePrediction.html', prediction=output)
    return render_template('generalDisease.html', form=form)
