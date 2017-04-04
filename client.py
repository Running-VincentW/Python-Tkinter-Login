from database import db
class client:
    def __init__(self,user_id):
        if(user_id == -1):
            #create dummy
            self.username = None
            self.is_admin = None
        else:
            result = db.getinfo(user_id)
            self.username = result[0][1]
            self.is_admin = (result[0][3]==1)
