from cProfile import label
import os
from tkinter import*
from PIL import Image,ImageTk
from student_registration import registrationclass
from time_table_admin import admintimetableclass
from admin_student_quary import studentsquaryclass
from admin_note import adminnoteclass

class SMS:
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
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1000,y=15,height=40,width=150)
        #=====Clock========#
        self.lbl_clock=Label(self.root,text="Welcome to Student Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#606060",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Left Menu======#
        self.MenuLogo=Image.open("images/student.png")
        self.MenuLogo=self.MenuLogo.resize((200,200)) 
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        left_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        left_Frame.place(x=0,y=120,width=200,height=585)

        lbl_MenuLogo=Label(left_Frame,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

        #===== Buttons ========#
        lbl_menu=Label(left_Frame,text="Menu",font=("times new roman",20),bg="#009688")
        lbl_menu.pack(side=TOP,fill=X)

        btn_reg=Button(left_Frame,text="Registration",command=self.student_registration,font=("times new roman",20,"bold"),bg="#6fc7d6",bd=3,cursor="hand2").place(x=0,y=240,relwidth=1,height=70)
        btn_details=Button(left_Frame,text="Time Table",command=self.Time_Table,font=("times new roman",20,"bold"),bg="#e3a664",bd=3,cursor="hand2").place(x=0,y=310,relwidth=1,height=70)
        btn_routine=Button(left_Frame,text="Note",command=self.admin_note_tab,font=("times new roman",20,"bold"),bg="#69cc4e",bd=3,cursor="hand2").place(x=0,y=380,relwidth=1,height=70)
        btn_note=Button(left_Frame,text="Student-Quary",command=self.admin_student_quary,font=("times new roman",20,"bold"),bg="#d16ded",bd=3,cursor="hand2").place(x=0,y=450,relwidth=1,height=70)
        btn_exit=Button(left_Frame,text="Exit",command=self.exit_btn,font=("times new roman",20,"bold"),bg="#d92537",bd=3,cursor="hand2").place(x=0,y=510,relwidth=1,height=70)


      #=====Footer======#
        lbl_footer=Label(self.root,text="SMS-Student Management System | Developed By Sandipan Mukherjee\n For any Technical Issue Contact: 894xxxx255",font=("times new roman",12),bg="#606060",fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)   

#=================== LINK TO STUDENT REGISTRATION =================================

    def student_registration(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=registrationclass(self.new_win)

#================== LINK TO DATA VIEW TAB ==========================================
    def Time_Table(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=admintimetableclass(self.new_win)

#================== LINK TO STUDENT'S QUARY TAB =====================================
    def admin_student_quary(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=studentsquaryclass(self.new_win)

#================== LINK TO note TAB ===============================================
    def admin_note_tab(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=adminnoteclass(self.new_win)

#================== LINK TO USER DASHBOAD TAB ==========================================
    def logout(self):
      self.root.destroy()
      os.system("python login_system.py")

#================== FUNCTION OF EXIT BTN ==========================================
    def exit_btn(self):
      self.root.destroy()



if __name__=="__main__":
  root=Tk()
  obj=SMS(root)
  root.mainloop()