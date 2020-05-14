from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from providers.models import Provider

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=4, max=6)])
    email = StringField('Email', validators=[DataRequired(),
                            Email()])
    phone_number = StringField('Phone number', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    specialty = StringField('Specialty', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                Length(min=6, max=12)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                        EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        provider = Provider.query.filter_by(username=username.data).first()
        if provider:
            raise ValidationError('That username is taken. Please choose another one.')

    def validate_email(self, email):
        provider = Provider.query.filter_by(email=email.data).first()
        if provider:
            raise ValidationError('That email is taken. Please choose another one.')

    def validate_phone_number(self, phone_number):
        provider = Provider.query.filter_by(phone_number=phone_number.data).first()
        if provider:
            raise ValidationError('That phone number belongs to someone else. Please use another one.')