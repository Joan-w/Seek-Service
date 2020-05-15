from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user
from seek import bcrypt, db
from seek.models import User, Provider
from seek.users.forms import RegistrationForm, SignupForm

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():    
    if current_user.is_authenticated:
        return redirect(url_for('provider.services'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        provider = Provider(username=form.username.data, email=form.email.data, phone_number=form.phone_number.data, password=hashed_password)
        db.session.add(provider)
        db.session.commit()
        flash('Your account has been successfully created! You are now available for booking services.', 'success')
        return redirect(url_for('main.home'))
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(signup_form.password.data).decode('utf-8')
        user = User(username=signup_form.username.data, email=signup_form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('home.html', form=form, signup_form=signup_form, title='Welcome to Seek-Service')

