from flask_wtf import FlaskForm
from core import db
from wtforms import StringField, PasswordField, DateField, TimeField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from wtforms.widgets import PasswordInput
from core.models import User

class LogForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators={DataRequired()})
    startTime = TimeField('Start Time', validators=[DataRequired()])
    endTime = TimeField('End Time', validators=[DataRequired()])
    miles = DecimalField('Miles', validators=[DataRequired()])
    avHR = IntegerField('Av. HR', validators=[DataRequired()])
    steps = IntegerField('Steps', validators=[DataRequired()])
    submit = SubmitField('Log Hike')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Enter Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter Password"}, widget=PasswordInput(hide_value=False))
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    city= StringField('City', validators=[DataRequired()])
    state= StringField('State', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.execute(db.select(User).filter_by(userName=username.data)).first()
        if user:
            raise ValidationError('User already exists.')

    def validate_email(self, email):
        email = db.session.execute(db.select(User).filter_by(emailAddress=email.data)).first()
        if email:
            raise ValidationError('Email is already registered.')