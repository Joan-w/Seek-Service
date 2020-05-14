from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from ..forms import LoginForm,RequestResetForm,ResetPasswordForm,RegistrationForm
from . import users
from .. import db
from ..utilis import send_reset_email


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "house booking service login"
    return render_template('login.html',login_form = login_form,title=title)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

#Reset password function
@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():  
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login')) 
    return render_template('reset_request.html', title='Reset Password', form=form) 

#Reset token function
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token): 
    user = User.verify_reset_token(token) 
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login')) 
    return render_template('reset_token.html', title='Reset Password', form=form)