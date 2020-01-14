from flask_wtf import Form
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField


class NoteDownForm(Form):
    note = PageDownField('Start writing notes...')
    submit = SubmitField('Submit')
