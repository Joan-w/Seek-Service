from flask import render_template
from app import app

# Views
@app.route('/')
def service():

    '''
    View root page function that returns the service page and its data
    '''
    return render_template('services.html')