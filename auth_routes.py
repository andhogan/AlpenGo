from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import User
from application import db, app, alpengo_data
from forms import LoginForm, RegistrationForm
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///alpengo.db')
Session = sessionmaker(bind=engine)
session=Session

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    # check if user actually exists
    for user in User:
        if username == user['userName'] and password == user['password']:

    # take the user supplied password, hash it, and compare it to the hashed password in database
    #if not user or not check_password_hash(User.password, password): 
        #flash('Login credentials invalid. Please try again.')
        #return redirect(url_for('auth.login')) 

    # if the above check passes, then we know the user has the right credentials
            user = User.userID
            login_user(user, remember=remember)
    return redirect(url_for('core.achievements'))

@auth.route('/register')
def signup():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@auth.route('/register', methods=['POST'])
def register():
    
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    cityState = request.form.get('city_state')

    user = engine.execute(text("SELECT emailAddress FROM User")) # if this returns a user, then the email already exists in database

    if user: # if a user is found  
        flash('Email address already exists, please log in.')
        return redirect(url_for('auth.login'))

    # create new user with hashed password
    new_user = User(emailAddress=email, firstName=firstname, lastName=lastname, userName=username, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))