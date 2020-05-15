from flask import render_template, flash, url_for, redirect
from application import db, app
from application.forms import RegistrationForm, LoginForm
from application.models import User


providers = [
    {
        'full_name' : 'Joan Kinyua',
        'username' : 'Joan',
        'county' : 'Nairobi',
        'specialty' : 'Interior designer',
        'bio' : 'I was born to be a designer. My designing techniques are all you need'
    },
    {
        'first_name' : 'Simon Mathu',
        'username' : 'Simon',
        'email' : 'mathu@gmail.com',
        'phone_number' : '023 456 789',
        'county' : 'Kitui',
        'specialty' : 'Plumber',
        'bio' : 'Fixing people\'s taps and make the happy makes me more happier.'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Welcome to Seek-Service')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data}, your account has been successfully created! You are now available for booking services.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='wamuyu@gmail.com' and form.password.data =='password':
            flash('Your login was successful.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsucessful!', 'danger')
    return render_template('login.html', title='Login', form=form)
