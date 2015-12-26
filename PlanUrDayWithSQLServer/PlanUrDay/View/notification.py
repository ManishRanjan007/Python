from flask.ext.wtf import Form
#from flask.ext.wtf.html5 import CalendarField
from wtforms.fields.html5 import DateTimeField as DateField1
from wtforms import widgets, StringField, BooleanField, PasswordField, SubmitField, DateTimeField, DateField
from wtforms_components import IntegerField
from wtforms.validators import DataRequired, NumberRange, Email
import flask, flask.views

    
class NotificationForm(Form):
    notificationId = StringField('notificationId')
    message = StringField('message', validators=[DataRequired()])
    #time_of_notification = DateField1('time_of_notification', format='%H-%M')
    #day_of_notification = StringField('day_of_notification', validators=[DataRequired()])
    repeat = BooleanField('repeat')
    #enable = widgets.CheckboxInput()
    enable = BooleanField('enable')
    submitNotification = SubmitField('Add Notification')
    #calendar = CalendarField()



