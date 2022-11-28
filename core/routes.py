from flask import render_template, url_for, flash, redirect, request
from core import app, db, bcrypt
from core.forms import LogForm, LoginForm, RegistrationForm
from core import alpengo_data
from core.models import user_achievement, user_peak, User, Peak, Achievement
from flask_login import login_user, current_user

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/peaks')
def peakselection():
    return render_template('peakselection.html', title='Peaks', peaks=alpengo_data.Peaks)

@app.route('/<peak>')
def peakpage(peak):
    userID = None
    peakID = None
    selected = None
    for p in alpengo_data.Peaks:
        if p['Name'] == peak:
            selected = p
            peakID = p['PeakID']
            break
    return render_template('peak.html', title=f'{peak}', peak=selected, userpeak=alpengo_data.UserPeaks[2])

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = LogForm()
    if form.validate_on_submit():
        flash('Your hike has been logged!', 'success')
        return redirect(url_for('achievements'))
    print(form.errors)
    return render_template('log.html', title='Log', form=form)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(userName=form.username.data)).scalar()
        print(user)
        if (user and bcrypt.check_password_hash(user.password, form.password.data)):
            login_user(user)
            return redirect(url_for('achievements',userID=user.userID))
        else:
            flash('Login failed.  Please try again.')
    return render_template('login.html', title='Login', form=form)


@app.route('/achievements')
@login_required
def achievements(userID):
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
                print(achievement)
                retList.append(achievement)
    return render_template('achievements.html', achieve_list=retList, title='Achievements', userID=current_user)