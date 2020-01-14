from flask import Blueprint, render_template, redirect, url_for
from manage_me.notes.forms import NoteDownForm

notes = Blueprint('notes', __name__)

@notes.route('/notes/new')
def notes_create():
    form = NoteDownForm()

    return render_template('notes_create.html', form=form)
    
