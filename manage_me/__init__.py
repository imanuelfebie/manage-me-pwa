from flask import Flask

# flask object
app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = '123456'

from manage_me.users.routes import users 

app.register_blueprint(users)
