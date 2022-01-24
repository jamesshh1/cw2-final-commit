from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# The Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '770022098636920ad892c570cbd0923343af21326dd8c943'
# Set the directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Set the database URI that should be used for connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
# Integrate SQLAlchemy to our application
db = SQLAlchemy(app)
# Configure the app with LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
# Import routes from blog
from blog import routes
