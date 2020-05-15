from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from seek import bcrypt, db
from seek.models import User, Provider
from seek.users.forms import RegistrationForm, LoginForm, SignupForm

users = Blueprint('users', __name__)


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


