from flask import Flask, render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user

# Create Route decorator
@app.route("/")

# Create route for home page
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

# Create route for post pages
@app.route("/post/<int:post_id>")
def post(post_id):
  post=Post.query.get_or_404(post_id)
  return render_template('post.html',title=post.title,post=post)

# Create route for register page
@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    # Check the form is valid when submitted and submit it to the database if so
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering!')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

# Create route for register page
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    # Check the form is valid when submitted
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password.')
    return render_template('login.html',title='Login',form=form)

# Create route to allow users to log out
@app.route("/logout")
def logout():
    logout_user()
    flash('Thank you for visiting.')
    return redirect(url_for('home'))

# Route for invalid URL
@app.errorhandler(404)
def page_not_found(e):
      return render_template('404.html'), 404

# Route for internal server error
@app.errorhandler(500)
def page_not_found(e):
      return render_template('500.html'), 500

# Attempt to create comment functionality on the posts
# comment = Comment()
# db.session.add(comment)
# db.session.commit()