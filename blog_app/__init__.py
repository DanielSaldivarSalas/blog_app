from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '14013659ae4a0a048de4a8054cea9096' #secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #ORM 
bcrypt = Bcrypt(app) #used to salt password hashes
login_manager = LoginManager(app) #handles user sessions
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from blog_app import routes
