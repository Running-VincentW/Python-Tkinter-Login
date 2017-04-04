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

