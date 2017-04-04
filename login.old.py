from tkinter import *
from database import db
class Login(object):
    def register(self):
        pass
    def check_password(self):
        self.user_id = db.getuserid(self.usEntry.get(),self.pwEntry.get())
        if(self.user_id == -1):
            self.login_failure()
        else:
            self.login_success()
    def login_success(self):
        self.lbl_status.set("Login succeed.")
        #self.newWindow = tk.Toplevel(self.master)
        #self.app = home(self.newWindow)
        pass
    def login_failure(self):
        self.lbl_status.set("Authentication failed.")
        self.wrongpass +=1
        if(self.wrongpass >= 3):
            self.btn_login.configure(state = DISABLED)
            self.lbl_status.set("Denied access.")
        pass
    def __init__(self,root):
        #initialize login frame
        self.wrongpass = 0
        self.frLogin = Frame(root, padx=20, pady=20)
        self.frLogin.grid(row=0,column=0) # Create a frame and set it's position

        Label(self.frLogin, text="Username").grid(row=0,column=0) #create the username label
        self.usEntry = Entry(self.frLogin) #create the entry login box
        self.usEntry.grid(row=0,column=1) #position the username box

        Label(self.frLogin, text="Password").grid(row=1,column=0) #create the password label
        self.pwEntry = Entry(self.frLogin, show="*") #create the password box
        self.pwEntry.grid(row=1,column=1) #position password box

        self.btn_login = Button(self.frLogin, borderwidth=4, text="Login", width=10, pady=4, command=self.check_password)
        self.btn_login.grid(row=2,column=1)
        self.lbl_status = StringVar(root)
        self.lbl_status.set("waiting input...")
        Label(self.frLogin,textvariable= self.lbl_status).grid(row=4,column=0,columnspan=2,sticky='W')

        #initialize register frame
        self.frReg = Frame(root, padx=20, pady=20)
        self.frReg.grid(row=0,column=0) # Create a frame and set it's position

        Label(self.frReg, text="Username").grid(row=0,column=0) #create the username label
        self.usEntry_reg = Entry(self.frReg) #create the entry login box
        self.usEntry_reg.grid(row=0,column=1) #position the username box

        Label(self.frReg, text="Password").grid(row=1,column=0) #create the password label
        self.pwEntry_reg1 = Entry(self.frReg, show="*") #create the password box
        self.pwEntry_reg1.grid(row=1,column=1) #position password box

        Label(self.frReg, text="re-enter Password").grid(row=2,column=0) #create the password label
        self.pwEntry_reg2 = Entry(self.frReg, show="*") #create the password box
        self.pwEntry_reg2.grid(row=2,column=1) #position password box
        
        Button(self.frReg, borderwidth=4, text="Register", width=10, pady=4, command=self.register).grid(row=3,column=1)


def main():
    try: userinit()
    except NameError: pass
    root = Tk()
    demo = Login(root)
    root.geometry('300x160') #set the dimensions of the window
    root.title('Login Screen')
    try: run()
    except NameError: pass
    root.mainloop()

if __name__ == '__main__': main()
