from flask import Flask, render_template, url_for, flash, redirect
from forms import LogForm
# Place Holder for form fucntion definitions
# from forms import 

app = Flask(__name__)

app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'

#############################################################
# Below is dummy data we can leverage during our development.
#############################################################
Users = [{
    'UserID': '1',
    'FirstName': 'Alex',
    'LastName': 'Jocius',
    'UserName': 'aljo',
    'EmailAddress': 'aljo@email.com',
    'Password': 'password',
    'Location': (30.266666, -97.733330),
    'TotalDistance': 150,
    'MountainsHiked': 5,
    'TotalTime': '25:00:00',
    'NoAchievements': 4,
    'TotalElevGain': 25000}, 
    {'UserID': '2',
    'FirstName': 'Andrew',
    'LastName': 'Hogan',
    'UserName': 'anho',
    'EmailAddress': 'anho@email.com',
    'Password': 'password1',
    'Location': (38.328732, -84.270020),
    'TotalDistance': 210,
    'MountainsHiked': 8,
    'TotalTime': '37:00:00',
    'NoAchievements': 7,
    'TotalElevGain': 34000},
    {'UserID': '3',
    'FirstName': 'Katie',
    'LastName': 'Sobczak',
    'UserName': 'kaso',
    'EmailAddress': 'kaso@email.com',
    'Password': 'password2',
    'Location': (40.014984, -105.270546),
    'TotalDistance': 185,
    'MountainsHiked': 6,
    'TotalTime': '32:00:00',
    'NoAchievements': 6,
    'TotalElevGain': 27500}
]

Peaks = [{
    'PeakID': 1,
    'Name': 'Mt Elbert',
    'Location': (39.151647, -106.412346),
    'StartElev': 9700,
    'SummitElev': 14438,
    'ElevGain': 5300,
    'Length': 11.00,
    'Avtime': 8.00,
    'RouteType': 'Out and Back',
    'Class': 2,
    'Description': 'The highest summit in Colorado, Mt Elbert offeres stunning views of the surrounding Rocky Mountains.'},
    {'PeakID': 2,
    'Name': 'Mt Evans',
    'Location': (39.588301, -105.643829),
    'StartElev': 12850,
    'SummitElev': 14268,
    'ElevGain': 1650,
    'Length': 5.25,
    'Avtime': 3.75,
    'RouteType': 'Out and Back',
    'Class': 3,
    'Description': 'Generally conisdered a challenging route, Mt Evans is one of six front range 14ers.  Keep an eye out for bighorn sheep and summer wildflowers.'},
    {'PeakID': 3,
    'Name': 'Capitol Peak',
    'Location': (39.1501, -107.0764),
    'StartElev': 9450,
    'SummitElev': 14138,
    'ElevGain': 5300,
    'Length': 17.00,
    'Avtime': 9.75,
    'RouteType': 'Out and Back',
    'Class': 4,
    'Description': 'Often called the most difficult 14er in Colorado, its rugged terrain and extreme slopes will prove to be a challenge for even the most experienced hikers.'},
    {'PeakID': 4,
    'Name': 'North Maroon Peak',
    'Location': (39.070663, -106.988937),
    'StartElev': 9590,
    'SummitElev': 14022,
    'ElevGain': 4500,
    'Length': 9.25,
    'Avtime': 7.00,
    'RouteType': 'Out and Back',
    'Class': 4,
    'Description': 'One of the most iconic 14ers in Colorado, this picturesque mountain is a technical challenge, challenging hikers with its rugged terrain and route-finding.'},
    {'PeakID': 3,
    'Name': 'Quandary Peak',
    'Location': (39.3972, -106.1064),
    'StartElev': 10850,
    'SummitElev': 14272,
    'ElevGain': 3450,
    'Length': 6.75,
    'Avtime': 5.25,
    'RouteType': 'Out and Back',
    'Class': 1,
    'Description': 'A beginner friendly summit, Quandary Peak is less than a two hour drive from Denver and offers panoramic views of the surrounding terrain.'},
]

Achievements = [{
    'AchievementID': 1,
    'Achievement': 'First Hike',
    'Description': 'You have successfully hiked your first mountain!'},
    {'AchievementID': 2,
    'Achievement': 'Weekend Warrior',
    'Description': "You've logged tons of miles on the weekend!"},
    {'AchievementID': 2,
    'Achievement': 'Weekend Warrior',
    'Description': "You've logged tons of miles on the weekend!"}
]

UserPeaks = [{
    'UserID': 1,
    'PeakID': 2,
    'Date': '01/10/2020',
    'StartTime': '05:30',
    'EndTime': '12:30',
    'Miles': 5.25,
    'AvHr': 135,
    'Steps': 7500},
    {'UserID': 1,
    'PeakID': 3,
    'Date': '05/10/2021',
    'StartTime': '04:47',
    'EndTime': '2:15',
    'Miles': 17.00,
    'AvHr': 152,
    'Steps': 32000},
    {'UserID': 2,
    'PeakID': 1,
    'Date': '10/10/2022',
    'StartTime': '03:15',
    'EndTime': '12:17',
    'Miles': 11.00,
    'AvHr': 127,
    'Steps': 22000},
    {'UserID': 3,
    'PeakID': 3,
    'Date': '03/25/2022',
    'StartTime': '06:12',
    'EndTime': '4:03',
    'Miles': 17.00,
    'AvHr': 117,
    'Steps': 32000}
]

UserAchievment = [{
    'UserID': 1,
    "AchievementID": 2},
    {'UserID': 2,
    "AchievementID": 1},
    {'UserID': 2,
    "AchievementID": 2},
    {'UserID': 2,
    "AchievementID": 3},
    {'UserID': 3,
    "AchievementID": 1},
    {'UserID': 3,
    "AchievementID": 2}
]

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
    return render_template('peakselection.html', title='Peaks', peaks=Peaks)

@app.route('/<peak>')
def peakpage(peak):
    userID = None
    peakID = None
    for p in Peaks:
        if p['Name'] == peak:
            selected = p
            peakID = p['PeakID']
            break
    return render_template('peak.html', title=f'{peak}', peak=selected, userpeak=UserPeaks[2])

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = LogForm()
    if form.validate_on_submit():
        flash('Your hike has been logged!', 'success')
        return redirect(url_for('home'))
    return render_template('log.html', title='Log', form=form)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogForm()
    if form.validate_on_submit():
        flash('Welcome!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', title='Achievements')

if __name__ == '__main__':
    app.run(debug=True)
