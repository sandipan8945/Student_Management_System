#from cProfile import label
from tkinter import*
import os
from login_system import loginsystemclass
from user_timetable import timetableclass
from PIL import Image,ImageTk
from user_note import usernoteclass
from login_system import loginsystemclass
from user_student_query import userqueryclass

class user_dashboadclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x785+0+0")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")

         #========Images=======
        self.background=ImageTk.PhotoImage(file="images/logo03.png")
        self.lbl_image=Label(self.root,image=self.background).place(x=0,y=0)

        #===TITLE===
        self.icon_title=PhotoImage(file="images\logo1.png")
        title=Label(self.root,text="Student Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #=======btn=======#
        btn_login=Button(self.root,text="Login as Admin",command=self.Login_System,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1000,y=15,height=40,width=150)

        #=====Clock========#
        self.lbl_clock=Label(self.root,text="Welcome to Student Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#606060",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Left Menu======#
        self.MenuLogo=Image.open("images/student.png")
        self.MenuLogo=self.MenuLogo.resize((200,200)) 
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        left_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        left_Frame.place(x=0,y=120,width=200,height=525)

        lbl_MenuLogo=Label(left_Frame,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

        #===== Buttons ========#
        lbl_menu=Label(left_Frame,text="Menu",font=("times new roman",20),bg="#009688")
        lbl_menu.pack(side=TOP,fill=X)

        btn_time=Button(left_Frame,text="Time Table",command=self.user_timetable,font=("times new roman",20,"bold"),bg="#6fc7d6",bd=3,cursor="hand2").place(x=0,y=240,relwidth=1,height=70)
        btn_details=Button(left_Frame,text="Note",command=self.user_note,font=("times new roman",20,"bold"),bg="#e3a664",bd=3,cursor="hand2").place(x=0,y=310,relwidth=1,height=70)
        btn_query=Button(left_Frame,text="Query",command=self.user_student_query,font=("times new roman",20,"bold"),bg="#69cc4e",bd=3,cursor="hand2").place(x=0,y=380,relwidth=1,height=70)
        btn_exit=Button(left_Frame,text="Exit",command=self.EXIT_BUTTON,font=("times new roman",250,"bold"),bg="#d92537",bd=3,cursor="hand2").place(x=0,y=450,relwidth=1,height=70)


      #=====Footer======#
        lbl_footer=Label(self.root,text="SMS-Student Management System | Developed By Sandipan Mukherjee\n For any Technical Issue Contact: 894xxxx255",font=("times new roman",12),bg="#606060",fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)   

#================== LINK TO TIME TABLE TAB ==========================================
    def user_timetable(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=timetableclass(self.new_win)

#================== LINK TO note TAB ==========================================
    def user_note(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=usernoteclass(self.new_win)

#================== LINK TO Student Query TAB ==========================================
    def user_student_query(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=userqueryclass(self.new_win)

  
#================== LINK TO LOGIN SYSTEM TAB ==========================================
    def Login_System(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=loginsystemclass(self.new_win)

#================== FUNCTION OF EXIT BTN ==========================================
    def EXIT_BUTTON(self):
      self.root.destroy()


if __name__=="__main__":
  root=Tk()
  obj=user_dashboadclass(root)
  root.mainloop()