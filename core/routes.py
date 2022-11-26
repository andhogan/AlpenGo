from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_required, current_user
from core import app, db
from core.forms import LogForm
from core import alpengo_data
from core.models import User

routes = Blueprint('routes', __name__)

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