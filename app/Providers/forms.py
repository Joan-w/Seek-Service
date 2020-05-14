from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=4, max=6)])
    email = StringField('Email', validators=[DataRequired(),
                            Email()])
    phone_number = StringField('Phone number', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    specialty = StringField('Specialty', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                Length(min=6, max=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                        EqualTo('password')])
    submit = SubmitField('Register')