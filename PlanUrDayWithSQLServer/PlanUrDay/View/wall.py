import flask, flask.views
import utils

class WallForm(flask.views.MethodView):
    @utils.login_required
    def get(self):
    notificationId = StringField('notificationId', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])
    time_of_notification = DateField('time_of_notification', format='%Y-%m-%d')
    day_of_notification = StringField('day_of_notification', validators=[DataRequired()])
    repeat = BooleanField('repeat')
    #enable = widgets.CheckboxInput()
    enable = BooleanField('enable')
    submitNotification = SubmitField('Submit')


