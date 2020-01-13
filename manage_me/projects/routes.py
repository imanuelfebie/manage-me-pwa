from flask import Blueprint, render_template, redirect, url_for

projects = Blueprint('projects', __name__)

@projects.route('/home')
def home():
    return render_template('home.html')
