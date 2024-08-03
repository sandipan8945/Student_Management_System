from tkinter import*
from tkinter import ttk,messagebox
from tkinter.font import BOLD
from turtle import bgcolor
from PIL import Image,ImageTk
import sqlite3

class usernoteclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="Note Section",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=20,width=980)

        self.var_date=StringVar()
        self.var_teachername=StringVar()
        self.txt_note=StringVar()

        #------ DATABASE FREAME------------------#

        std_Frame=LabelFrame(self.root,bg="white")
        std_Frame.place(x=35,y=80,width=980,height=350)

        scrolly=Scrollbar(std_Frame,orient=VERTICAL)
        scrollx=Scrollbar(std_Frame,orient=HORIZONTAL)

      
        self.admin_note_table=ttk.Treeview(std_Frame,columns=("date","teachername","note"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.admin_note_table.xview)

        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.admin_note_table.yview)

        self.admin_note_table.heading("date",text="Date")
        self.admin_note_table.heading("teachername",text="Teacher's Name")
        self.admin_note_table.heading("note",text="Note")
  
        self.admin_note_table["show"]='headings'

        
        self.admin_note_table.pack(fill=BOTH,expand=1)

        self.admin_note_table.column("date",width=100)
        self.admin_note_table.column("teachername",width=110)
        self.admin_note_table.column("note",width=110)
        self.admin_note_table.pack(fill=BOTH,expand=1)
        self.admin_note_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        
#===========================================================================#
#======================= DATABASE CONNECTION ================================#

    #----------- Show Data in Database Table ------------#
    
    def show(self):
      con=sqlite3.connect(database=r'std_query.db')
      cur=con.cursor()
      try:
        cur.execute("select* from std_note")
        rows=cur.fetchall()
        self.admin_note_table.delete(*self.admin_note_table.get_children())
        for row in rows:
          self.admin_note_table.insert('',END,values=row)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  #---------- Data View ---------------#

    def get_data(self,ev):
      f=self.admin_note_table.focus()
      content=(self.admin_note_table.item(f))
      row=content['values']
  
      self.var_date.set(row[0]),
      self.var_teachername.set(row[1]),
      self.txt_note.set(row[2]),
  

if __name__=="__main__":
  root=Tk()
  obj=usernoteclass(root)
  root.mainloop()