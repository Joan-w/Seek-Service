from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from seek.models import User, Provider

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=4, max=6)])
    email = StringField('Email', validators=[DataRequired(),
                            Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                            Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=4, max=6)])
    email = StringField('Email', validators=[DataRequired(),
                            Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
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
