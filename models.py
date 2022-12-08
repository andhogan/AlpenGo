from flask import url_for, redirect
from core import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None


class User(db.Model, UserMixin):
    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    emailAddress = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_id(self):
        return (str(self.userID))

    def __repr__(self):
        return f"User('{self.userID}', '{self.firstName}', '{self.lastName}', '{self.userName}', '{self.emailAddress}', '{self.password}')"

class Peak(db.Model):
    peakID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    startElevation = db.Column(db.Integer, nullable=False)
    summitElevation = db.Column(db.Integer, nullable=False)
    elevationGain = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Float, nullable=False)
    avTime = db.Column(db.Float, nullable=False)
    routeType = db.Column(db.String(120), nullable=False)
    peakClass = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Peak('{self.peakID}', '{self.name}', '{self.startElevation}', '{self.summitElevation}', '{self.elevationGain}', '{self.length}', '{self.avTime}', \
                '{self.routeType}', '{self.peakClass}', '{self.description}')"
                

class Achievement(db.Model):
    achievementID = db.Column(db.Integer, primary_key=True)
    achievement = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return f"Achievement('{self.achievementID}', '{self.achievement}', '{self.description}')"

class userPeak(db.Model):
    userPeakID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    peakID = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    startTime = db.Column(db.Time, nullable=False)
    endTime = db.Column(db.Time, nullable=False)
    miles = db.Column(db.Float, nullable=False)
    avHR = db.Column(db.Integer, nullable=False)
    steps = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"userPeak('{self.userID}', '{self.peakID}', '{self.date}', '{self.startTime}', '{self.endTime}', '{self.miles}', '{self.avHR}', \
                '{self.steps}')"


class userAchievement(db.Model):
    userAchievementID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    achievementID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"userAchievement('{self.userID}', '{self.achievementID}')"