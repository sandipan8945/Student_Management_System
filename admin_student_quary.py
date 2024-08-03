from ast import Delete
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
#from user_student_query import userqueryclass
import sqlite3

class studentsquaryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_date=StringVar()
        self.var_studentname=StringVar()
        self.txt_query=StringVar()


        title=Label(self.root,text="Student's Query",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=20,width=980)


        #===== Time Table Details =========#
        #------- Making Database Table --------#


        std_Frame=Frame(self.root,bd=3,relief=GROOVE,bg="white")
        std_Frame.place(x=35,y=80,width=980,height=380)

        scrolly=Scrollbar(std_Frame,orient=VERTICAL)
        scrollx=Scrollbar(std_Frame,orient=HORIZONTAL)

        self.timetable=ttk.Treeview(std_Frame,columns=("date","studentname","query"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.timetable.xview)

        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.timetable.yview)

        self.timetable.heading("date",text="Date")
        self.timetable.heading("studentname",text="Student Name")
        self.timetable.heading("query",text="Query")

        self.timetable["show"]='headings'

        
        self.timetable.pack(fill=BOTH,expand=1)

        self.timetable.column("date",width=100)
        self.timetable.column("studentname",width=110)
        self.timetable.column("query",width=110)
        self.timetable.pack(fill=BOTH,expand=1)
        self.show()


#===========================================================================#
#======================= DATABASE CONNECTION ================================#

    #----------- Show Data in Database Table ------------
    
    def show(self):
      con=sqlite3.connect(database=r'std_query.db')
      cur=con.cursor()
      try:
        cur.execute("select* from Query_Table")
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
  
      self.var_date.set(row[0]),
      self.var_studentname.set(row[1]),
      self.txt_query.set(row[2]),
    

if __name__=="__main__":
  root=Tk()

  obj=studentsquaryclass(root)
  root.mainloop()