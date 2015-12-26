from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField, DateTimeField, DateField
from wtforms_components import IntegerField
from wtforms.validators import DataRequired, NumberRange, Email
import flask, flask.views


class SignUpForm(Form):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    mobile_numb = IntegerField('mobile_numb', validators = [NumberRange(min=1000000000, max=9999999999)])
    #dob123 = DateTimeField('dob',validators=[DataRequired(), 'Enter Date'])
    dob123 = DateField('dob', format='%Y-%m-%d')
    emailID = StringField('EmailID',validators = [Email('Enter valid email')])
    password = PasswordField('password', validators = [DataRequired()])
    c_password = PasswordField('c_password', validators = [DataRequired()])
    signUpBTN = SubmitField('Sign Up')

