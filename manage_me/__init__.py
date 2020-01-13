from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

# flask object
app = Flask(__name__)

# database instance
db = SQLAlchemy(app)

# secret key
app.config['SECRET_KEY'] = '123456'

from manage_me.users.routes import users 
from manage_me.universities.routes import universities
from manage_me.projects.routes import projects

app.register_blueprint(users)
app.register_blueprint(universities)
app.register_blueprint(projects)
