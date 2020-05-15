from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from seek import bcrypt, db
from seek.models import User, Provider
from seek.users.forms import RegistrationForm, LoginForm, SignupForm

users = Blueprint('users', __name__)

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.services'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('signup.html', title='SignUp', form=form)

@users.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('provider.services'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('provider.services'))
        else:
            flash('Invalid username or Password', 'danger')
    title = "house booking service login"
    return render_template('login.html',form = form, title=title)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("provider.services"))

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        provider = Provider(username=form.username.data, email=form.email.data, phone_number=form.phone_number.data, password=hashed_password)
        db.session.add(provider)
        db.session.commit()
        flash('Your account has been successfully created! You are now available for booking services.', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title = "Register", form=form)
