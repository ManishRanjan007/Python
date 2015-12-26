from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import flask, flask.views

users = {'jake':'bacon'}

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    #remember_me = BooleanField('remember_me', default=False)
    loginBTN = SubmitField('login')
    logoutBTN = SubmitField('logout')

