from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LogForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], format='%m-%d-%Y')
    startTime = TimeField('Start Time', validators=[DataRequired()])
    endTime = TimeField('End Time', validators=[DataRequired()])
    miles = DecimalField('Miles', validators=[DataRequired()])
    avHR = IntegerField('Av. HR', validators=[DataRequired()])
    steps = IntegerField('Steps', validators=[DataRequired()])
    submit = SubmitField('Log Hike')