from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # validate_<field_name> methods automatically apply to the fields
    def validate_username(self, usrnm):
        usr = User.query.filter_by(username=usrnm.data).first()
        if usr is not None:
            raise ValidationError("Username already taken")

    def validate_email(self, emlads):
        usr = User.query.filter_by(email=emlads.data).first()
        if usr is not None:
            raise ValidationError("Email address already taken")

