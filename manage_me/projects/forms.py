from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class ProjectCreateForm(FlaskForm):
    name = StringField('Project name', validators=[DataRequired()])
    due_date = DateField('Due data')
    submit = SubmitField('Add')


class MilestoneCreateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    #projects = SelectField()
    due_date = DateField()
    submit = SubmitField('New Milestone')
