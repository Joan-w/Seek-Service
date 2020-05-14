from flask import Flask, url_for, render_template, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6d6f17faad7ed099602b06c4aa7837dc'


providers = [
    {
        'first_name' : 'Joan',
        'last_name' : 'Kinyua',
        'username' : 'Joan',
        'email' : 'muyu@gmail.com',
        'phone_number' : '123 456 789',
        'county' : 'Nairobi',
        'specialty' : 'Interior designer',
        'bio' : 'I was born to be a designer. My designing techniques are all you need'
    },
    {
        'first_name' : 'Simon',
        'last_name' : 'Mathu',
        'username' : 'Simon',
        'email' : 'mathu@gmail.com',
        'phone_number' : '023 456 789',
        'county' : 'Kitui',
        'specialty' : 'Plumber',
        'bio' : 'Fixing people\'s taps and make the happy makes me more happier.'
    }
]


@app.route('/providers')
def service_providers():
    return render_template('providers.html', title = "Service Providers", providers=providers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # provider = Provider(first_name=form.first_name.data, last_name=form.last_name.data, 
        #                     username=form.username.data, email=form.email.data, 
        #                     phone_number=form.phone_number.data, county=form.county.data, 
        #                     specialty=form.specialty.data, bio=form.bio.data, password=hashed_password)
        # db.session.add(provider)
        # db.session.commit()
        flash('Your account has been successfully created! You are now available for booking services.', 'success')
        return redirect(url_for('service_providers'))
    return render_template('register.html', title = "Register", form=form)

if __name__ == '__main__':
    app.run(debug=True)