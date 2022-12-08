from flask import render_template, url_for, flash, redirect, request
from core import app, db, bcrypt
from core.forms import LogForm, LoginForm, RegistrationForm
from core import alpengo_data
from core.models import userAchievement, userPeak, User, Peak, Achievement
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy import func
from decimal import *


# Home Page of the application.
@app.route('/')
def home():
    return render_template('home.html', title='Home')


# About Page highlighting overall function of site and authors.
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# Peaks Page displaying a list of 14er Peaks offered in the site.
@app.route('/peaks')
def peakselection():
    if current_user.is_authenticated:
        userID = current_user.userID
    else:
        userID = None
    peaks = db.session.execute(db.select(Peak)).scalars()
    if userID:
        user_peaks = db.session.execute(db.select(userPeak.peakID).filter_by(userID=userID)).scalars().all()
    else:
        user_peaks = None
    if not user_peaks:
        user_peaks=None
    return render_template('peakselection.html', title='Peaks', peaks=peaks, userpeaks=user_peaks)


# Displays the selection of the specific peak on the Peaks Page, displaying Mountain Peak stats & User stats
@app.route('/peaks/<peak>')
@login_required
def peakpage(peak):
    if current_user.is_authenticated:
        userID = current_user.userID
    else:
        userID = None
    peak_select = db.session.execute(db.select(Peak).filter_by(name=peak)).scalar()
    peakID = peak_select.peakID
    user_peaks = db.session.execute(db.select(userPeak).filter_by(userID=userID, peakID=peakID)).scalar()
    return render_template('peak.html', title=f'{peak}', peak=peak_select, userpeak=user_peaks)


# Log Hike Page where a user can input data on a specific hike.
@app.route('/<peak>/log', methods=['GET', 'POST'])
@login_required
def log(peak):
    miles = 0
    if current_user.is_authenticated:
        user_ID = current_user.userID
    else:
        user_ID = None
    peak_select = db.session.execute(db.select(Peak).filter_by(name=peak)).scalar()
    peak_ID = peak_select.peakID
    form = LogForm(request.form)
    if form.validate_on_submit():
        userData = userPeak(userID=user_ID, peakID=peak_ID, date=form.date.data, startTime=form.startTime.data, endTime=form.endTime.data, miles=form.miles.data, avHR=form.avHR.data, steps=form.steps.data)
        db.session.add(userData)
 

        if db.session.execute(db.select(userAchievement).filter_by(userID=user_ID, achievementID=1)).scalar() == None:
            print("hello")
            print(db.session.execute(db.select(userAchievement).filter_by(userID=user_ID, achievementID=1)).scalar())
            userFirst = userAchievement(userID=user_ID, achievementID=1)
            db.session.add(userFirst)


        a = Decimal(userData.miles)
        b = Decimal(10.00)
        if b.compare(a) == -1 and (db.session.execute(db.select(userAchievement).filter_by(userID=user_ID, achievementID=3)).scalar() == None):
            userMiles = userAchievement(userID=user_ID, achievementID=3)
            db.session.add(userMiles)

        numHikes = db.session.query(userPeak.peakID).filter_by(userID=user_ID).distinct().count()
        print(numHikes)


        if numHikes and (numHikes > 4) and not db.session.execute(db.select(userAchievement).filter_by(userID=user_ID, achievementID=2)).scalar():
            userHalf = userAchievement(userID=user_ID, achievementID=2)
            db.session.add(userHalf)

        numSteps = db.session.query(func.sum(userPeak.steps).filter(userPeak.userID==user_ID)).all()
        if numSteps and numSteps[0][0] > 100000 and not db.session.execute(db.select(userAchievement).filter_by(userID=user_ID, achievementID=4)).scalar():
            userSteps = userAchievement(userID=user_ID, achievementID=4)
            db.session.add(userSteps)

        db.session.commit()
        db.session.close()

        flash('Your hike has been logged!', 'success')
        return redirect(url_for('peakpage', peak=peak))
    return render_template('log.html', title='Log', form=form)


# Register Page where users can register for the site.
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstName=form.firstname.data, lastName=form.lastname.data, userName=form.username.data, emailAddress=form.email.data, password=password_hashed)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        logUser = db.session.execute(db.select(User).filter_by(userName=form.username.data)).scalar()
        login_user(logUser)
        flash('Thank you! Your account has been registered.', 'success')
        return redirect(url_for('achievements', userID=logUser.userID))
    return render_template('register.html', title='Register', form=form)


# Login Page where users can login to their account.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(userName=form.username.data)).scalar()
        if (user and bcrypt.check_password_hash(user.password, form.password.data)):
            login_user(user)
            flash('Welcome Back!', 'success')
            return redirect(url_for('achievements',userID=user.userID))
        else:
            flash('Login failed. Please try again.')
    return render_template('login.html', title='Login', form=form)


# Logout link displayed in navbar to logout user.
@app.route('/logout')
def logout():
    logout_user()
    flash('You are now logged out.', 'success')
    return redirect(url_for('home'))


# Achievments Page highlighting a user's achievements as determined by the logged data.
@app.route('/achievements')
@login_required
def achievements():
    if current_user.is_authenticated:
        user_ID = current_user.userID
    else:
        user_ID = None
    user_achievements = db.session.execute(db.select(userAchievement.achievementID).filter_by(userID=user_ID)).scalars().all()
    if user_achievements:
        achievements = [db.session.query(Achievement).filter_by(achievementID=id).scalar() for id in user_achievements]
    else: 
        achievements = None
    return render_template('achievements.html', achieve_list=achievements, title='Achievements')