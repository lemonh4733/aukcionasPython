from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=24)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=80), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    conf_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=24)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class AddItemForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=4, max=80)])
    category = StringField('Category', validators=[DataRequired(), Length(min=4, max=80)])
    description = StringField('Description', validators=[DataRequired(), Length(min=4, max=80)])
    country = StringField('Country', validators=[DataRequired(), Length(min=4, max=80)])
    min_price = IntegerField('Minimum Price', validators=[DataRequired(), Length(min=4, max=80)])
    auction_image = FileField('Photo', validators=[DataRequired()])
    end_day = DateField(label='End time',validators=[DataRequired()],format = "%Y-%m-%d")
    time = IntegerField('Time', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Add')
class BidForm(FlaskForm):
    offer = IntegerField('Enter your bid', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Add')
