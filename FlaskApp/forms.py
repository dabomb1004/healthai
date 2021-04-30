from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, widgets, SelectMultipleField, SelectField, TextAreaField, IntegerField, StringField, StringField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Regexp
from FlaskApp.models import User, HeartDiseasePrediction, BreastCancer, LiverDisease, GeneralDisease
import pandas as pd

data = [('Yes','Yes'), ('No','No'), ('Do Not Disclose','Do Not Disclose')]
gender = [(1,'Male'), (0,'Female')]
chest_pain = [(1,"Low"), (2,"Moderate"), (3,"High"), (4,"Severe")]
thal = [(0,'0'), (1,'1'), (2, '2'), (3,'3')]
ecg = [(0, '0'), (1,'1'), (2,'2')]
angina = [(1, 'Yes'), (0, 'No')]

#creating choices for the general symptom assessment
df1 = pd.read_csv('FlaskApp/static/Symptom-severity.csv')
symptom_choices_edited = []
symptom_choices = df1['Symptom'].unique()
for x in symptom_choices:
    add = []
    add.append(x)
    new_string = x.replace("_", " ")
    add.append(new_string)
    add = tuple(add)
    symptom_choices_edited.append(add)



class BreastForm(FlaskForm):
    texture_mean = StringField('Please enter the texture mean', validators=[DataRequired()])
    perimeter_mean = StringField('Please enter the perimeter mean', validators=[DataRequired()])
    smoothness_mean = StringField('Please enter the smoothness mean', validators=[DataRequired()])
    compactness_mean = StringField('Please enter the compactness mean', validators=[DataRequired()])
    concavity_mean = StringField('Please enter the concavity mean', validators=[DataRequired()])
    concave_points_mean = StringField('Please enter the concave points mean', validators=[DataRequired()])
    symmetry_mean = StringField('Please enter the symmetry mean', validators=[DataRequired()])
    radius_se = StringField('Please enter the radius se', validators=[DataRequired()])
    compactness_se = StringField('Please enter the compactness se', validators=[DataRequired()])
    concavity_se = StringField('Please enter the concavity se', validators=[DataRequired()])
    concave_points_se = StringField('Please enter the cancave points se', validators=[DataRequired()])
    texture_worst = StringField('Please enter the texture worst', validators=[DataRequired()])
    smoothness_worst = StringField('Please enter the smoothness worst', validators=[DataRequired()])
    compactness_worst = StringField('Please enter the compactness worst', validators=[DataRequired()])
    concavity_worst = StringField('Please enter the concavity worst', validators=[DataRequired()])
    concave_points_worst = StringField('Please enter the concave points worst', validators=[DataRequired()])
    symmetry_worst = StringField('Please enter the symmetry worst', validators=[DataRequired()])
    fractal_dimension_worst = StringField('Please enter the fractal dimension worst', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20, message="Maximum num of characters is 20")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp("^(0|[1-9][0-9]*)$", message="Only numbers and no dashes")])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    # Address =  StringField('Address', validators=[DataRequired()])
    db_day =  StringField('Date of Birth: Day', validators=[DataRequired(), Regexp("^(0|[1-9][0-9]*)$", message="Day must be a number")])
    db_month =  StringField('Date of Birth: Month', validators=[DataRequired(), Regexp("^(0|[1-9][0-9]*)$", message="Month must be a number")])
    db_year =  StringField('Date of Birth: Year', validators=[DataRequired(), Regexp("^(0|[1-9][0-9]*)$", message="Year must be a number")])
    ssn =  StringField('SSN', validators=[DataRequired(),Regexp("^(0|[1-9][0-9]*)$", message="SSN must be a number")])
    password = PasswordField('Password', validators=[DataRequired(),
            Length(min=8, message="Password be at least 8 characters"),
            Regexp("^(?=.*[a-z])", message="Password must have a lowercase character"),
            Regexp("^(?=.*[A-Z])", message="Password must have an uppercase character"),
            Regexp("^(?=.*\\d)", message="Password must contain a number"),
            Regexp("(?=.*[@$!%*#?&])", message="Password must contain a special character")])

    password2= PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('password')])
    bp = SelectField(u'Have you ever been diagnosed with high blood pressure?', choices=data,  option_widget=widgets.CheckboxInput())
    diabetes = SelectField(u'Do you have diabetes?', choices=data,  option_widget=widgets.CheckboxInput())
    smoke = SelectField(u'Do you smoke?', choices=data, option_widget=widgets.CheckboxInput())
    terms = BooleanField('Terms', validators=[DataRequired()])
    privacy = BooleanField('privacy', validators=[DataRequired()])
    consent = BooleanField('consent', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user= User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp("^(0|[1-9][0-9]*)$", message="Only numbers and no dashes")])
    submit = SubmitField('Submit')
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class BasePrediction(FlaskForm):
    Age=IntegerField('Age', validators=[DataRequired()])
    Gender= SelectField(u'Select Your Gender (1=Male, 0=Female)', choices=gender,  option_widget=widgets.CheckboxInput(), validators=[DataRequired()])
    ChestPain= SelectField(u'Choose the Level of Chest Pain', choices=chest_pain,  option_widget=widgets.CheckboxInput(), validators=[DataRequired()])
    BloodPressure= IntegerField('What is your resting blood pressure?', validators=[DataRequired()])
    ElectrocardiographicResults= SelectField(u'Resting Electrocardiographic Results', choices=ecg,  option_widget=widgets.CheckboxInput(), validators=[DataRequired()])
    MaxHeartRate= IntegerField('Maximum Heart Rate Recieved', validators=[DataRequired()])
    ExerciseInducedAngina= SelectField('Have you experienced angina or pain in the heart from exercising?', choices=angina,  option_widget=widgets.CheckboxInput(), validators=[DataRequired()])
    STdepression= StringField('ST depression induced by exercise relative to rest', validators=[DataRequired()])
    MajorVesselsNo= IntegerField('The number of major vessels colored by flouroscopy (Values 0-4)', validators=[DataRequired()])
    Thalassemia=SelectField(u'Thalassemia', choices=thal,  option_widget=widgets.CheckboxInput(), validators=[DataRequired()])

    submit = SubmitField('Submit')

class LiverPrediction(FlaskForm):
    Age= IntegerField('Enter Your Age', validators=[DataRequired()])
    Gender= SelectField(u'Select Your Gender', choices=gender,  option_widget=widgets.CheckboxInput(), validators=[DataRequired()])
    Total_Bilirubin= StringField('Enter Total Bilirubin', validators=[DataRequired()])
    Direct_Bilirubin=  StringField('Enter Direct Bilirubin', validators=[DataRequired()])
    Alkaline_Phosphotase= IntegerField('Enter Alkaline Phospotase', validators=[DataRequired()])
    Alamine_Aminotransferase= IntegerField('Enter Alkaline Phospotase', validators=[DataRequired()])
    Aspartate_Aminotransferase= IntegerField('Enter Aspartate Aminotransferase', validators=[DataRequired()])
    Total_Protiens= StringField('Enter Total Protiens', validators=[DataRequired()])
    Albumin= StringField('Enter Albumni', validators=[DataRequired()])
    Albumin_and_Globulin_Ratio= StringField('Enter Albumin and Globulin Ratio', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GenDiseasePrediction(FlaskForm):
    Symptom1= SelectField(u'Select A Symptom', choices=symptom_choices_edited,   validators=[DataRequired()])
    Symptom2= SelectField(u'Select A Symptom', choices=symptom_choices_edited,   validators=[DataRequired()])
    Symptom3= SelectField(u'Select A Symptom', choices=symptom_choices_edited,  validators=[DataRequired()])
    Symptom4= SelectField(u'Select A Symptom', choices=symptom_choices_edited,  validators=[DataRequired()])
    Symptom5= SelectField(u'Select A Symptom', choices=symptom_choices_edited,   validators=[DataRequired()])
    submit = SubmitField('Submit')
    def validate(self):
        if not FlaskForm.validate(self):
            return False
        result = True
        seen = set()
        for field in [self.Symptom1, self.Symptom2, self.Symptom3, self.Symptom4, self.Symptom5]:
            if field.data in seen:
                field.errors.append('Please select five distinct choices.')
                result = False
            else:
                seen.add(field.data)
        return result
