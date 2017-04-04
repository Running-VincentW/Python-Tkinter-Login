import datetime as dt
import sqlite3
class db:
    def sql(sql,data):
        with sqlite3.connect('logins.db') as db:
            cursor = db.cursor()
            cursor.execute(sql,data)
            return (cursor.fetchall())
            db.commit()
    def getuserid(username,password):
        auth = db.sql("SELECT `userId` FROM `logins` WHERE `username` = ? AND `passwd` = ?",(username,password))
        if (len(auth)==0):return -1
        else: return auth[0][0]
    def isadmin(user_id):
        auth = db.sql("SELECT `is_admin` FROM `logins` WHERE `userId` = ?",(user_id,))
        if(auth[0][0]==0):return False
        else:
            return True
    def register(username,password):
        db.sql("INSERT INTO `logins`(`username`,`passwd`) VALUES (?,?)",(username,password))
        return
    def getinfo(userid):
        return db.sql("SELECT * FROM `logins` WHERE `userId` = ?",(userid,))
    def user_sales_timeline(userid): #column 1 = date, column 2 = sales amt
        result = db.sql("SELECT DATE(SaleDate) AS 'Date', SUM(SaleValue) FROM Sales WHERE User = ? GROUP BY Date ORDER BY Date",(userid,))
        plot = [[],[]]
        for c in result:
            plot[0].append(c[0])
            plot[1].append(c[1])
        plot[0] = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in plot[0]]
        return plot
    def sales_pie_chart():
        result = db.sql("SELECT (SELECT username FROM logins WHERE userId = User), SUM(SaleValue)*100/(SELECT SUM(SaleValue) FROM Sales) FROM Sales GROUP BY User",())
        plot = [[],[]]
        for c in result:
            plot[0].append(c[0])
            plot[1].append(c[1])
        return plot

