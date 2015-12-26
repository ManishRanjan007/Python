#!C:\Python34\python.exe

import pypyodbc as conn

class DBConnection:
       
        def connectDB():
            server = 'MCMRAN01.eur.ad.sag\SQLEXPRESS'
            database = 'PlanUrDay'
            username = 'PlanUrDay'
            password = 'PlanUrDay'
    
            db = conn.connect(driver='{SQL Server}', server='mcmran01.eur.ad.sag\\N_SQLEXPRESS2012', database=database, user=username, password=password, trusted_connection='yes')
  
            cursor = db.cursor()
            print(cursor)
            return db,cursor





    
