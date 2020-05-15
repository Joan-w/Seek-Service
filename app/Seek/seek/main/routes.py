from flask import render_template, flash, url_for, redirect, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title='Welcome to Seek-Service')

