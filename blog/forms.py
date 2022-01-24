from flask_wtf import FlaskForm
from sqlalchemy import String
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp
from blog.models import User

# Build a form which allows users to register and define the appropriate fields
class RegistrationForm(FlaskForm):
  # Only allow user names which are 4 and 20 characters long and can only contain lowercase letters
  username = StringField('First name',validators=[DataRequired(),Regexp('^[a-z]{4,20}$',message='Your username should be between 4 and 20 characters long, and can only contain lowercase letters.')])
  # Only allow valid email address formats    
  email = StringField('Email',validators=[DataRequired(), Regexp('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message='Please enter a valid email address.')])
  password = PasswordField('Password',validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
  password2 = PasswordField('Confirm password',validators=[DataRequired()])
  submit = SubmitField('Register')
  # Check if username already exists to then ensure all usernames are unique
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('This Username already exist. Please choose a different one.')

# Log in form
class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

# Attempt to create comment functionality on the posts
# class PostForm(FlaskForm):
#     post = StringField('post', validators=[DataRequired()])
#     title = StringField('title', validators=[DataRequired()])
# class CommentForm(FlaskForm):
#     comment = StringField('post', validators=[DataRequired()])