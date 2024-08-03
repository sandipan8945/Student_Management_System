from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import os

class loginsystemclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | developed By Sandipan")
        self.root.geometry("1530x785+0+0")
        
        #========Images=======
        self.background=ImageTk.PhotoImage(file="images/log2.png")
        self.lbl_image=Label(self.root,image=self.background).place(x=0,y=0)

        #===== login Frame ======
        self.username=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Email-id",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="#cbd1cc").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_password=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#cbd1cc").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgrey").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",font=("times new roman",15,"bold"),fg="lightgrey").place(x=150,y=357)

        btn_forgot=Button(login_frame,text='Forget Password',font=('times new roman',13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="red").place(x=110,y=390)

        #======== Frame2 ===========
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_register=Label(register_frame,text="Don't have an account ?",font=("times new roman",13),bg="white").place(x=40,y=17)
        btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="red").place(x=220,y=16)

    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.username.get()!="Admin" or self.password.get()!="12345":
            messagebox.showerror("Error","Invalid username or password\nTry again with correct credentials")
        else:
            answer=messagebox.askquestion("Sample","Do you want to preced?")
            if answer == 'yes':
                self.root.destroy()
                os.system("python admin_dashboad.py")
            else:
                self.root.quit(loginsystemclass)
             

root=Tk()
obj=loginsystemclass(root)
root.mainloop()