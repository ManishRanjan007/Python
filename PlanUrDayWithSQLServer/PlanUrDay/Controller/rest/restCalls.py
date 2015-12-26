from flask import Flask, jsonify, abort, make_response, request
import json
app = Flask(__name__)

import sys
sys.path.insert(0, 'D:/Python/PlanUrDay/Model/db')
import Users as users
import notifications as notify

@app.route('/selectUsers', methods=['GET'])
def getUsers():
    usersDetails = users.SelectUsers.selectAllUsers()
    userDetails_dict = []
    for user in usersDetails:
        userDetail_dict = {
                'firstname' : user[1],
                'lastname' : user[2],
                'Mobile Number' : user[3]
            }
        userDetails_dict.append(userDetail_dict)
    if len(userDetails_dict) == 0:
        abort(404)
    return jsonify({'user' : userDetails_dict})

@app.route('/validateUser', methods=['POST'])
def validateUser():
    if not request.json:
        abort(400)

    try:
        
        userDetails = users.SelectUsers.selectUserWhereMobileNo(int(request.json.get('mobileno')), request.json.get('password'))
        userDetail_dict = []
        for detail in userDetails:
            user_details = {
                    'userId' : detail[0],
                    'firstname' : detail[1],
                    'mobileNo' : detail[3],
                    'emailId' : detail[5]
                }
            print("%%%%%%%%%%%%%%")
            print(detail[1])
        if detail is None:
            return jsonify({'User' : 'Authentication Failed'}), 401
        print(userDetails)
        return jsonify({'user_details' : user_details}), 201
    except Exception as e:
        print(e)
        print("========Invalid LOgin===========")
        return jsonify({'User' : 'Authentication Failed'}), 401

@app.route('/addUser', methods=['POST'])
def addUser():
    print("----------Inside Add User ====")
    if not request.json:
        abort(400)
    print(request.data)
    users.InsertIntoUsers.insertUsers(request.json.get('firstname'), request.json.get('lastname'), request.json.get('mobileno'), request.json.get('dob'), request.json.get('emailid'), request.json.get('password'))
    return jsonify({'Result': 'Inserted'}),201

@app.route('/addUserNoification', methods=['POST'])
def addUserNotification():
    print("----------Inside Add User Notification ====")
    if not request.json:
        abort(400)
    print(request.data)
    notify.InsertIntoNotification.insertNotification(request.json.get('mobileNo'), request.json.get('message'), request.json.get('timeOfNotification'), request.json.get('repeat'), request.json.get('enable'))
    return jsonify({'Result': 'Notification Added'}),201

@app.route('/selectUserNotifications', methods=['POST'])
def getUserNotifications():
    print("******Inside get user notifications********")
    userNotifications = notify.SelectUsersNotifications.selectNotificationsWhereMobileNo(request.json.get('mobileNo'))
    print(request.json.get('mobileNo'))
    userNotifications_dict = []
    for notification in userNotifications:
        userNotification_dict = {
                'mobileNo' : notification[1],
                'message' : notification[2],
                'time' : notification[3],
                'repeat' : notification[4],
                'enable' : notification[5]
            }
        userNotifications_dict.append(userNotification_dict)
    if len(userNotifications_dict) == 0:
        print("*******Aborting******")
        abort(404)
    return jsonify({'userNotification' : userNotifications_dict}), 201


@app.route('/updateNotification', methods=['POST'])
def updateNotification():
    print("----------Inside Add User ====")
    if not request.json:
        abort(400)
    print(request.data)
    notify.UpdateNotification.updateNotification(request.json.get('notificationId'), request.json.get('mobileNo'),  request.json.get('message'), request.json.get('time'), request.json.get('repeat'), request.json.get('enable'))
    return jsonify({'Result': 'Notification Updated'}),201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
app.run(debug=True)
