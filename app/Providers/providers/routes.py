from flask import url_for, render_template, redirect, flash
from providers import app, bcrypt, db
from providers.forms import RegistrationForm
from providers.models import Provider

providers = [
    {
        'full_name' : 'Joan Kinyua',
        'username' : 'Joan',
        'email' : 'muyu@gmail.com',
        'phone_number' : '123 456 789',
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

@app.route('/providers')
def service_providers():
    # image_file = url_for('static', filename='profile_pics/' + current_user.image_file), image_file=image_file
    return render_template('providers.html', title = "Service Providers", providers=providers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('service_providers'))
    form = RegistrationForm()
    if form.validate_on_submit():
        provider = Provider(username=form.username.data, email=form.email.data, phone_number=form.phone_number.data, county=form.county.data, 
                            specialty=form.specialty.data, bio=form.bio.data)
        db.session.add(provider)
        db.session.commit()
        flash('Your account has been successfully created! You are now available for booking services.', 'success')
        return redirect(url_for('service_providers'))
    return render_template('register.html', title = "Register", form=form)
