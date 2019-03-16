from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from blog_app.models import User

class RegistrationForm(Form):
    username = StringField('Username', 
                            validators=[
                                DataRequired(),
                                Length(min=2, max=20)
                                ]
                            )
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email() # makes sure it's a email format
                        ])
    password = PasswordField('Password',
                            validators=[
                                DataRequired()
                            ])
    confirm_password = PasswordField('Confirm Password',
                            validators=[
                                DataRequired(),
                                EqualTo('password')
                            ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        #if username exists, raise erorr 
        if user:
            raise ValidationError('Username is taken, choose another one')
    
    def validate_email(self, email):

        email = User.query.filter_by(email=email.data).first()

        #if email is taken , raise erorr 
        if email:
            raise ValidationError('Email is already in use, choose another one')


class LoginForm(Form):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email() # makes sure it's a email format
                        ])
    password = PasswordField('Password',
                            validators=[
                                DataRequired()
                            ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')