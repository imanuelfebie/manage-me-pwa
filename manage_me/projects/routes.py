from flask import Blueprint, render_template, redirect, url_for
from manage_me.projects.forms import ProjectCreateForm, MilestoneCreateForm

projects = Blueprint('projects', __name__)

@projects.route('/home')
def home():
    '''Homescreen with projects overview'''
    return render_template('home.html')

@projects.route('/projects/new')
def project_create():
    '''Create new project'''
    form = ProjectCreateForm()
    return render_template('project_create.html', form=form)

@projects.route('/milestone/create')
def milestone_create():
    form = MilestoneCreateForm()
    return render_template('milestone_create.html', form=form)
    

