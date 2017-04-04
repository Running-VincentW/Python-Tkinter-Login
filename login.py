from tkinter import *
from database import db
from client import client
class mainUI(Frame):
    def logout(self):
        self.controller.user = client(-1)
        self.controller.show_frame("LoginFrame")
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.welcome_msg = StringVar(parent)
        Label (self,textvariable = self.welcome_msg).grid(row=1,column=1,sticky='NW')
        Button (self, text="Logout", command=self.logout).grid(row=1,column=2,sticky='NE')
        self.content = StringVar()
        Label (self,textvariable = self.content).grid(row=2,column=1,columnspan=2,sticky='NSEW')
    def refresh(self):
        self.welcome_msg.set("Hello %s!" %self.controller.user.username)
        if(self.controller.user.is_admin):
            self.content.set("You are a admin!")
        else:
            self.content.set("You are a user.")
        
class RegisterFrame(Frame):
    def refresh(self):
        self.pass1.set('')
        self.pass2.set('')
        self.usEntry_reg.set('')
    def create_account(self):
        if(self.pass1.get()!=self.pass2.get()):
            self.pass1.set('')
            self.pass2.set('')
            messagebox.showwarning("Password not match.","Please verify your password again.")
        elif(self.pass1.get() == ''):
            messagebox.showwarning("Blank fields.","Please do not leave any fields blank.")
        else:
            try:
                db.register(self.usEntry_reg.get(),self.pass1.get())
                messagebox.showinfo("Account created.","Please login using new credentials. :)")
            except:
                messagebox.showwarning("Error.","Please try another username or contact a technician")
            self.controller.show_frame("LoginFrame")
            self.controller.frames['LoginFrame'].usEntry.set(self.usEntry_reg.get())
    def __init__(self,parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.usEntry_reg = StringVar(parent)
        Label(self, text="Username").grid(row=0,column=0) #create the username label
        Entry(self, textvariable = self.usEntry_reg).grid(row=0,column=1) #position the username box

        self.pass1 = StringVar(parent)
        self.pass1.set('')
        self.pass2 = StringVar(parent)
        self.pass2.set('')
        
        Label(self, text="Password").grid(row=1,column=0)
        Entry(self, show="*", textvariable=self.pass1).grid(row=1,column=1)

        Label(self, text="re-enter Password").grid(row=2,column=0)
        Entry(self, show="*", textvariable=self.pass2).grid(row=2,column=1)

        Button(self, borderwidth=4, text="Register", width=10, pady=4, command=self.create_account).grid(row=3,column=1)
        Button(self, borderwidth=4, text="Return", width=10, pady=4, command=lambda: self.controller.show_frame("LoginFrame")).grid(row=4,column=1)
class LoginFrame(Frame):
    def refresh(self):
        self.pwEntry.set('')
        self.lbl_status.set("IDLE.")
        self.usEntry.set('')
    def check_password(self):
        self.user_id = db.getuserid(self.usEntry.get(),self.pwEntry.get())
        self.pwEntry.set('')
        if(self.user_id == -1):
            self.login_failure()
        else:
            self.usEntry.set('')
            self.login_success()
    def login_success(self):
        self.lbl_status.set("Login succeed.")
        self.controller.user = client(self.user_id)
        self.controller.show_frame("mainUI")
        
    def login_failure(self):
        self.lbl_status.set("Authentication failed.")
        self.wrongpass +=1
        if(self.wrongpass >= 3):
            self.btn_login.configure(state = DISABLED)
            self.lbl_status.set("Denied access.")
        
    def __init__(self,parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.wrongpass = 0
        #self = Frame(root, padx=20, pady=20)
        self.grid(row=0,column=0) # Create a frame and set it's position
        self.usEntry = StringVar()
        self.pwEntry = StringVar()
        Label(self, text="Username").grid(row=0,column=0) #create the username label
        Entry(self,textvariable = self.usEntry).grid(row=0,column=1)

        Label(self, text="Password").grid(row=1,column=0) #create the password label
        Entry(self, show="*",textvariable = self.pwEntry).grid(row=1,column=1)

        self.btn_login = Button(self, borderwidth=4, text="Login", width=10, pady=4, command=self.check_password)
        self.btn_login.grid(row=2,column=1,columnspan=2)
        self.lbl_status = StringVar(parent)
        self.lbl_status.set("waiting input...")
        Button(self, borderwidth=4, text="Register", width=10, pady=4, command=lambda: self.controller.show_frame("RegisterFrame")).grid(row=3,column=1,columnspan=2)
        
        Label(self,textvariable= self.lbl_status).grid(row=4,column=0,columnspan=2,sticky='W')
class SampleApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.user = client(-1)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginFrame, RegisterFrame,mainUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        try:
            frame.refresh()
        except AttributeError:
            pass
        frame.tkraise()

class Login(Tk):
    def register(self):
        pass
    

def main():
    app = SampleApp()
    app.mainloop()

if __name__ == '__main__': main()
