from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_pagedown import PageDown

# flask object
app = Flask(__name__)

page_down = PageDown(app)

# database instance
db = SQLAlchemy(app)

# secret key
app.config['SECRET_KEY'] = '123456'

from manage_me.users.routes import users 
from manage_me.universities.routes import universities
from manage_me.projects.routes import projects
from manage_me.notes.routes import notes
from manage_me.preferences.routes import preferences
from manage_me.pwa.routes import pwa

app.register_blueprint(users)
app.register_blueprint(universities)
app.register_blueprint(projects)
app.register_blueprint(notes)
app.register_blueprint(preferences)
app.register_blueprint(pwa)
