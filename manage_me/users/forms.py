from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
        BooleanField)
from wtforms.validators import DataRequired, Email, EqualTo

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    login = SubmitField('Login')


class UserRegistrationForm(FlaskForm):
    firstname = StringField("Firstname", validators=[])
    lastname = StringField("Lastname", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm password', validators=[DataRequired(), EqualTo(password1)])
    register = SubmitField('Register')

