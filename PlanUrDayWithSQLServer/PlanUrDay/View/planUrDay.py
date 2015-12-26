from flask import render_template, redirect
import settings
from login import LoginForm
from signup import SignUpForm
from notification import NotificationForm
import flask
import callPostServices as callPost
import simplejson as json
import utils
import requests

app = flask.Flask(__name__)
app.config.from_object('settings')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        userDetails = callPost.callPostServices("127.0.0.1", 5000, {"Content-type": "application/json", "Accept": "application/json"}, {'mobileno': form.username.data, 'password': str(form.password.data)} ,"/validateUser")
        print(userDetails.status)
        
        if userDetails.status == 201:
            flask.flash('Login requested for Username="%s", Password=%s' %(form.username.data, str(form.password.data)))
            flask.session['username'] = form.username.data
            user_details = (json.loads(userDetails.read().decode('utf-8'))).get("user_details")
            #print(".............")
            #print(details.get("user_details").get("firstname"))
            flask.session['userId'] = user_details.get("userId")
            flask.session['firstname'] = user_details.get("firstname")
            flask.session['userId'] = user_details.get("emailId")
            return wall()
    if form.logoutBTN.data:
        flask.session.pop('username')
    
    return render_template('login.html',form=form)

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    signUpForm = SignUpForm()
    if signUpForm.signUpBTN.data and signUpForm.validate_on_submit():
        signUpFormData = signUpForm.data;
        date = signUpFormData.get('dob123')
        callPost.callPostServices("127.0.0.1", 5000, {"Content-type": "application/json",
        "Accept": "application/json"}, {'firstname': signUpFormData.get('firstname'), 'lastname': signUpFormData.get('lastname'), 'mobileno': signUpFormData.get('mobile_numb'), 'dob': str(date), 'emailid':signUpFormData.get('emailID'), 'password': signUpFormData.get('password') } ,"/addUser")
        return login()
    return render_template('signUp.html',form=signUpForm)    
        
@app.route('/addNotification', methods=['GET','POST'])
@utils.login_required
def addNotification():
    print("Inside Notification XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    notificationForm = NotificationForm()
    
    if notificationForm.submitNotification.data and notificationForm.validate_on_submit():
        print("Data Validated")
        print(flask.request.form.get('datetime123'))
        datetime = flask.request.form.get('datetime123');
        callPost.callPostServices("127.0.0.1", 5000, {"Content-type": "application/json",
        "Accept": "application/json"}, {'mobileNo': flask.session['username'], 'message': notificationForm.data.get('message'), 'timeOfNotification': str(datetime), 'repeat': notificationForm.data.get('repeat'), 'enable': notificationForm.data.get('enable')},"/addUserNoification")
        return redirect(("/wall"))
    #wall()
    return render_template('notification.html', form = notificationForm)


@app.route('/wall', methods=['GET', 'POST'])
@utils.login_required
def wall():
    print("**************")
    print(flask.session['username'])
    response = callPost.callPostServices("127.0.0.1", 5000, {"Content-type": "application/json",
        "Accept": "application/json"}, {'mobileNo':flask.session['username']} ,"/selectUserNotifications")
    print(response.status)
    if response.status == 201:
        print("Status 201")
        userNotifications = (json.loads(response.read().decode('utf-8'))).get("userNotification")
    else:
        print("inside else")
        userNotifications = None
    return render_template('wall.html',notifications=userNotifications) 
    
@app.route('/about', methods=['GET','POST'])
def showAbout():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def showContact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run(port=5001)
