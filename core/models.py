from core import db
from werkzeug.security import generate_password_hash, check_password_hash

user_achievement = db.Table('userAchievement', 
    db.Column('userID', db.Integer, db.ForeignKey('user.userID')),
    db.Column('achievementID', db.Integer, db.ForeignKey('achievement.achievementID'))
    )

user_peak = db.Table('userPeak', 
    db.Column('userID', db.Integer, db.ForeignKey('user.userID')),
    db.Column('peakID', db.Integer, db.ForeignKey('peak.peakID')),
    db.Column('date', db.Date, nullable=False),
    db.Column('startTime', db.Time, nullable=False),
    db.Column('endTime', db.Time, nullable=False),
    db.Column('miles', db.Float, nullable=False),
    db.Column('avHR', db.Integer, nullable=False),
    db.Column('steps', db.Integer, nullable=False),
)

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    emailAddress = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    achievements = db.relationship("Achievement", secondary=user_achievement, backref='user', lazy=True)
    peaks = db.relationship("Peak", secondary=user_peak, backref = 'peak', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method= 'sha256')
    
    def check_password (self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f"User('{self.firstName}', '{self.lastName}', '{self.userName}', '{self.emailAddress}')"

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
        return f"Peak('{self.name}', '{self.startElevation}', '{self.summitElevation}', '{self.description}')"

class Achievement(db.Model):
    achievementID = db.Column(db.Integer, primary_key=True)
    achievement = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Peak('{self.achievement}', '{self.description}')"
