from flask import Blueprint, render_template, redirect, url_for
from manage_me.users.forms import UserLoginForm, UserRegistrationForm

users = Blueprint('users', __name__)

@users.route('/login')
@users.route('/', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    return render_template('login.html', form=form)

@users.route('/register')
def register():
    form = UserRegistrationForm()

    return render_template('register.html', form=form)
