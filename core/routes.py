from flask import render_template, url_for, flash, redirect, request
from core import app, db, bcrypt
from core.forms import LogForm, LoginForm, RegistrationForm
from core import alpengo_data
from core.models import user_achievement, user_peak, User, Peak, Achievement
from flask_login import login_user, current_user, login_required, logout_user


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
        user_peaks = db.session.execute(db.select(user_peak).filter_by(userID=userID)).scalars()
    else:
        user_peaks = None
    return render_template('peakselection.html', title='Peaks', peaks=peaks, user_peaks=user_peaks)


# Displays the selection of the specific peak on the Peaks Page, displaying Mountain Peak stats & User stats
@app.route('/<peak>')
@login_required
def peakpage(peak):
    if current_user.is_authenticated:
        userID = current_user.userID
    peak_select = db.session.execute(db.select(Peak).filter_by(name=peak)).scalar()
    peakID = peak_select.peakID
    user_peaks = db.session.execute(db.select(user_peak).filter_by(userID=userID, peakID=peakID)).scalar()
    return render_template('peak.html', title=f'{peak}', peak=peak_select, userpeak=user_peaks)


# Log Hike Page where a user can input data on a specific hike.
@app.route('/<peak>/log', methods=['GET', 'POST'])
@login_required
def log(peak):
    if current_user.is_authenticated:
        user_ID = current_user.userID
    peak_select = db.session.execute(db.select(Peak).filter_by(name=peak)).scalar()
    peak_ID = peak_select.peakID
    form = LogForm()
    if form.validate_on_submit():
        userPeak = user_peak(userID=user_ID, peakID=peak_ID, date=form.date.data, startTime=form.startTime.data, endTime=form.endTime.data, miles=form.miles.data, avHR=form.avHR.data, steps=form.steps.data)
        db.session.add(userPeak)
        db.session.commit()
        flash('Your hike has been logged!', 'success')
        return redirect(url_for('achievements'))
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
        flash('Thank you! Your account has been registered.', 'success')
        return redirect(url_for('login'))
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
    userID = current_user.userID
    achieveID=None
    achieve_list=[]
    for achieves in alpengo_data.UserAchievement:
        if achieves['UserID'] == userID:
            achieveID=achieves['AchievementID']
            achieve_list.append(achieveID)
    retList = []
    for a in achieve_list:
        for achievement in alpengo_data.Achievements:
            if (a == achievement['AchievementID']):
                retList.append(achievement)
    return render_template('achievements.html', achieve_list=retList, title='Achievements')