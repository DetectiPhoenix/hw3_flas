from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
	cityName = StringField("City Name")
	submit = SubmitField("Submit")
