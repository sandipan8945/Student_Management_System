from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class timetableclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()


        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_day=StringVar()
        self.var_time=StringVar()
        self.var_sub=StringVar()
        self.var_tname=StringVar()
  


         #------ SEARCH FREAME------------------
        searchFrame=LabelFrame(self.root,text="Search Days",font=("goudy old style",12,"bold"),bg="white")
        searchFrame.place(x=35,y=50,width=450,height=70)
      
        #------Options------
        txt_search=Label(searchFrame,text="Days",font=("goudy old",15),bg="white").place(x=20,y=6)
        cmb_search=ttk.Combobox(searchFrame,values=("Select","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"),state='readonly',justify=CENTER,font=("goudy old",15))
        cmb_search.place(x=95,y=6,width=180)
        cmb_search.current(0)

        
        btn_search=Button(searchFrame,command=self.search,text="Search",font=("Arial",15),bg="crimson",fg="white",cursor="hand2").place(x=290,y=5,width=150,height=30)

        #--------- Title --------
        title=Label(self.root,text="Class Routine",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=20,width=980)


        #===== Time Table Details =========#
        #------- Making Database Table --------#


        std_Frame=Frame(self.root,bd=3,relief=GROOVE,bg="white")
        std_Frame.place(x=35,y=130,width=980,height=350)

        scrolly=Scrollbar(std_Frame,orient=VERTICAL)
        scrollx=Scrollbar(std_Frame,orient=HORIZONTAL)

        self.timetable=ttk.Treeview(std_Frame,columns=("day","time","sub","teacherName"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.timetable.xview)

        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.timetable.yview)

        self.timetable.heading("day",text="DAY")
        self.timetable.heading("time",text="TIME")
        self.timetable.heading("sub",text="SUBJECT")
        self.timetable.heading("teacherName",text="TEACHER'S NAME")

        self.timetable["show"]='headings'

        
        self.timetable.pack(fill=BOTH,expand=1)

        self.timetable.column("day",width=100)
        self.timetable.column("time",width=110)
        self.timetable.column("sub",width=110)
        self.timetable.column("teacherName",width=110)
        self.timetable.pack(fill=BOTH,expand=1)
        self.show()


#===========================================================================#
#======================= DATABASE CONNECTION ================================#

    #----------- Show Data in Database Table ------------
    
    def show(self):
      con=sqlite3.connect(database=r'nothing.db')
      cur=con.cursor()
      try:
        cur.execute("select* from Test_TimeTable")
        rows=cur.fetchall()
        self.timetable.delete(*self.timetable.get_children())
        for row in rows:
          self.timetable.insert('',END,values=row)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  #---------- Data View ---------------

    def get_data(self,ev):
      f=self.timetable.focus()
      content=(self.timetable.item(f))
      row=content['values']
  
      self.var_day.set(row[0]),
      self.var_time.set(row[1]),
      self.var_sub.set(row[2]),
      self.var_tname.set(row[3]),

  #---------- SEARCH BUTTON FUNCTION ----------------------
    def search(self):
      con=sqlite3.connect(database=r'nothing.db')
      cur=con.cursor()
      try:
        if self.var_searchby.get()=="Select":
          messagebox.showerror("Error","Select Search By option",parent=self.root)
    
        else:
          cur.execute("select* from Test_TimeTable where day=?",(self.var_searchby.get(),))  #.. Its the search quary....
          rows=cur.fetchone()
          if len(rows)!=0:
            self.timetable.delete(*self.timetable.get_children())
            for row in rows:
              self.timetable.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found",parent=self.root)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__":
  root=Tk()
  obj=timetableclass(root)
  root.mainloop()



  '''
  ---PROBLEM---

  SEARCH BUTTON PROBLEM
  '''