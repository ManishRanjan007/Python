#!C:\Python34\python.exe

from db_Connection import DBConnection as dbConnect

class InsertIntoNotification:
       
        
        def insertNotification(mobileNo, message, timeOfNotification, repeat, enable):
                sql = """INSERT INTO [dbo].[Notification]
           ([Mobile_No_FK]
           ,[Message]
           ,[Time]
           ,[Repeat]
           ,[Enable])
                VALUES ('{0}','{1}','{2}','{3}','{4}')""".format(mobileNo, message, timeOfNotification, repeat, enable)
                print("----------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()



class SelectUsersNotifications:
        
       
        def selectNotificationsWhereMobileNo(mobileNo):
                sql = "select * from [dbo].[Notification] where Mobile_No_FK = '{0}'".format(mobileNo)
                db, cursor = dbConnect.connectDB()
                userNotifications = cursor.execute(sql)
                return userNotifications

        def selectAllNotifications():
                sql = "select * from [dbo].[Notification]"
                db, cursor = dbConnect.connectDB()
                allNotifations = cursor.execute(sql)
                return allNotifations

        def selectAllNotificationsWhereEnableAndTime(fromTime, toTime):
                sql = """SELECT [Id]
      ,[Mobile_No_FK]
      ,[Message]
      ,cast([Time] as time)[Time]
        ,cast([Time] as date)[Date]
      ,[Repeat]
      ,[Enable]
        FROM [PlanUrDay].[dbo].[Notification] where [Enable] = 'true' and cast([Time] as time) > cast('{0}' as time) and cast([Time] as time) < cast('{1}' as time)""".format(fromTime, toTime)
                print("-----------------")
                print(sql)
              #  "select * from [dbo].[Notification] where [Enable] = 'true' and time > '{0}' and time < {1}".format(time,time)
                db, cursor = dbConnect.connectDB()
                allNotifations = cursor.execute(sql)
                return allNotifations
        

        
class UpdateNotification:
       

        def updateMsg(mobileNo, message, notificationId):
                sql = """UPDATE [dbo].[Notification]
                       SET [message] = '{0}' where [Mobile_Number] = '{1}' and [Id] = '{2}'""".format(message, mobileNo, notificationId)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()
                
        def updateNotificationStatus(mobileNo, notificationId, enable):
                sql = """UPDATE [dbo].[Notification]
                       SET [enable] = '{0}' where [Mobile_Number] = '{1}' and [Id] = '{2}'""".format(enable, mobileNo, notificationId)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()

        
        def updateNotification(notificationId, mobileNo, message, time, repeat, enable):
                sql = """UPDATE [dbo].[Notification]
                       SET [Message] = '{0}', [Time] = '{1}', [Repeat] = '{2}', [Enable] = '{3}' where [Id] = '{4}' and [mobileNo] = '{5}'""".format(message, time, repeat, enable, notificationId, mobileNo)
                print("---------" + sql)
                db, cursor = dbConnect.connectDB()
                cursor.execute(sql)
                db.commit()
                
#def printUserdetails(userDetails):
#        for userD in userDetails:
#                print(userD[1])


#notifications = SelectUsersNotifications.selectAllNotificationsWhereEnableAndTime("20:23:00", "20:26:00")
#for noti in notifications:
#        print(noti[2])
