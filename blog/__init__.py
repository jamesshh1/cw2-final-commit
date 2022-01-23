from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '770022098636920ad892c570cbd0923343af21326dd8c943'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes
