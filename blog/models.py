from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Create a model for posts to be stored in the database
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.Text, nullable=False)
  summary = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
  image_file = db.Column(db.String(40), nullable=False, default='test1.jpg')
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.date}', '{self.title}', '{self.content}')"

# Create a model for users to be stored in the database

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(20), unique=True, nullable=False)
  hashed_password=db.Column(db.String(120))
  post = db.relationship('Post', backref='user', lazy=True)

  def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.password}')"
  
  # Define password function
  @property
  def password(self):
    raise AttributeError('Password is not readable.')

  # Generate a hashed password from the password given by user
  @password.setter
  def password(self,password):
    self.hashed_password=generate_password_hash(password)

  # Check hashed password goes with inputted password
  def verify_password(self,password):
    return check_password_hash(self.hashed_password,password)

  
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(140))
#     author = db.Column(db.String(32), db.ForeignKey('user.username'), nullable=False)
#     timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

#     def __repr__(self):
#         return '<Post %r>' % (self.body)