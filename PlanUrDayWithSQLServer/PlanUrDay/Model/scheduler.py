#!C:\Python34\python.exe

import time
import datetime
import sendMessage
from threading import Timer
import sys
sys.path.insert(0, 'D:/Python/PlanUrDay/Model/db')
from notifications import SelectUsersNotifications
def print_time():
    print ("From print_time" + str(time.time()))




def checkNotifications():
    #time123 = time.strftime("%H:%M");
    fromTime = datetime.datetime.now()
    toTime = fromTime - datetime.timedelta(minutes=2)
    print(str(toTime))
    fromTime1 = str(fromTime.hour) + ":" + str(fromTime.minute) + ":" + "00"
    toTime1 = str(toTime.hour) + ":" + str(toTime.minute) + ":" + "00"
    print("******************************")
    print(fromTime1)
    print(toTime1)
    notifications = SelectUsersNotifications.selectAllNotificationsWhereEnableAndTime(toTime1, fromTime1)
    for notification in notifications:
        print(notification[5])
        if str(notification[5]).strip() == 'False' and notification[4] == time.strftime("%Y-%m-%d"):
            sendMessage.sendMessage(str(notification[1]),str(notification[2]))
        if str(notification[5]).strip() == str('True'):
            print("inside if ")
            sendMessage.sendMessage(str(notification[1]),str(notification[2]))
            
def print_some_times():
    checkNotifications()
    print (time.time())
    Timer(60, print_some_times, ()).start()
    #Timer(10, print_time, ()).start()
    #time.sleep(11)  # sleep while time-delay events execute
    #print (time.time())

print_some_times()

