# healthai
Health AI is my capstone project for the MSIST Program at GWU. It uses machine learning models such as CNN, Bagging Classifiers, &amp; SVM to predict the likelihood of having disease based on customer health input


# Installation 

To install the files and make them work in your local file you will need to do the following: 

Create VirtualEnv for Python 3-- For me I used windows. However, you can find the virtualenv installation instructions for other types here: https://phoenixnap.com/kb/install-flask
For Windows
If you don't have Python 3 installed please go to https://www.python.org/downloads/release/python-373/ and download python 3.7.3
1. Download the zip file and unzip in your local directory 
2. Open command line in administrative mode (right click on command line icon and choose run as admin)
3. go into the FlaskApp base directory: 
   cd C:\Users\test\Documents\FlaskApp   Note: this is my base directory path, you need to replace this with your's
4. Create Environment 
   py -3 -m venv <name of environment>  Note: I do py -3 m venv venv (venv is the name of environ but you can call it what you want) 
6. Activate the environment:
   venv\bin\activate (in this case venv is the name of my environ. Also this is for Windows for linux use . venv/bin/activate or use source in place of .)
7. Now that you are in your virtual environment install Python Flask: 
   pip install Flask 
  
8. Now All the packages are already installed inside of the venv folder in this github. However if you type in 'flask run' in the command line and get an error saying a package is missing or you would like to install these packages yourself Go on to Install Required Packages section below. If not, head on over to Run Website section. 

# Install Required Packages 

Originally I pip freezed all the requirements into a requirements.txt file but some things were off so I created another txt file 

1. Go to the main FlaskApp directory where app.py and config.py reside in the command line 
2. Once there do: 
   pip install -r actual_requirements.txt
In the case, you run into an error, you may need to pip install the packages listed in this txt file one by one. Make sure that scikit-learn==0.22.2.post1

# Run Website 
1. Now with all packages installed run the following: 
   flask run
2. You should see: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   Note: You may see cudart64_110.dll not found but you can ignore this as you might not have a gpu or the gpu driver installed for tensorflow. We won't need it since pickled    the already trained models for this project 
3. copy and paste the http://127.0.0.1:5000/ address and you should see the html render for the website 

# Setting Up the Database

1. If you would like to access more than just the status page and login into the main app you will need to set up a mysql database. For this projet a mariadb database version 8.0.20 was used. It would probably be wise to use version 8 or there may be compatibility issues.
2. If you are creating an RDS instance from AWS then make sure to make publicly accessible which is found under the Additional Configuration tab in setup. 
3. For the AWS RDS option, you need to go into the config file and edit the SQLALCHEMY_DATABASE_URI
4. Replace the contents with your own personal RDS info:
    
   SQLALCHEMY_DATABASE_URI = mysql://MASTER_USERNAME:PASSWORD@ENDPOINT:PORT#/healthai
   
   MASTER_USERNAME is the master username of the database 
   PASSOWORD is the password for the database you set on creation 
   ENDPOINT usually looks something like: healthai.adsadfsdfle.us-east-1.rds.amazonaws.com
   PORT# is usually 3306 but check your configuration
   
 5. Now if everything is set up properly, run the following in the main FlaskApp directory: 
    flask db init
 6. And now do: 
    flask db migrate
 7. Finally upgrade the database using the models found in models.py in FlaskApp/FlaskApp/models.py
 8. Now you should be able to login to the website and also access the assessment portal and get a health assessment for liver disease, heart disease, or pneumonia 
   
   

   
