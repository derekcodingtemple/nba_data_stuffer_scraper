from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DataForm(FlaskForm):
    search = StringField()
    submitData = SubmitField('Scrape Data')

class SessionForm(FlaskForm):
    submitSession = SubmitField('CLEAR SESSION')

class CSVForm(FlaskForm):
    submitCSV = SubmitField('Save to CSV')

class CronjobForm(FlaskForm):
    submitCronjob = SubmitField("SET CRONJOB")