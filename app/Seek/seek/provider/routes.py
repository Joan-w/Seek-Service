from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from seek import db
from seek.models import Provider
from seek.provider.forms import BookingForm

provider = Blueprint('provider', __name__)


@provider.route('/providers')
@login_required
def providers():
    return render_template('providers.html', title='Welcome to Seek-Service')

@provider.route('/services')
@login_required
def services():
    return render_template('services.html', title='Welcome to Seek-Service')

@provider.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    form = BookingForm()
    if form.validate_on_submit():
        flash('Your booking has been recorded! You will receive an email shortly with the booking details.', 'success')
        return redirect(url_for('provider.services'))
    return render_template('order.html', title='Booking well completed', form=form)