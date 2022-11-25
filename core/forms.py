from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TimeField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import PasswordInput

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
    city_state= StringField('City, State', validators=[DataRequired()])
    submit = SubmitField('Register')