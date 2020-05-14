from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)


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
def providers():
    return render_template('providers.html', title = "Service Providers", providers=providers)

@app.route('/register')
def register():
    title = '<h1>Boss Bitch</h1>'
    return title

if __name__ == '__main__':
    app.run(debug=True)