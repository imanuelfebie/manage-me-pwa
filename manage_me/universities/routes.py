from flask import Blueprint, render_template, redirect, url_for

universities = Blueprint('universities', __name__)

@universities.route('/course/list')
def course_list():
    
    return render_template('course_list.html')

@universities.route('/course/detail')
def course_detail():
    return render_template('course_detail.html')
