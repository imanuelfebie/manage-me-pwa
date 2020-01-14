from flask import Blueprint, render_template, redirect, url_for

preferences = Blueprint('preferences', __name__)

@preferences.route('/preferences')
def user_preferences():
    return render_template('preferences.html')
