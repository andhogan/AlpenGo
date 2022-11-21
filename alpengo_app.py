import alpengo_data
import connexion
from flask import Flask, render_template, url_for, flash, redirect
from forms import LogForm, LoginForm, RegistrationForm
# Place Holder for form fucntion definitions
# from forms import 

app = Flask(__name__)
#app = connexion.App(__name__, specification_dir="./")
#app.add_api("swagger.yml")

app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'

#############################################################
# Below is dummy data we can leverage during our development.
#############################################################

# Moved data to alpengo_data.py

#############################################
############ End of Dummy Data ##############
#############################################

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
    return render_template('log.html', title='Log', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Thank you!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Welcome!', 'success')
        return redirect(url_for('achievements'))
    return render_template('login.html', title='Login', form=form)

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', title='Achievements')

if __name__ == '__main__':
    app.run(debug=True)
