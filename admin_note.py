from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class adminnoteclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_date=StringVar()
        self.var_teachername=StringVar()
        #self.var_note=StringVar()


        title=Label(self.root,text="Note Section",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=20,width=980)


        #======= Row1 =======#
        lbl_date=Label(self.root,text="Date",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=90)
        txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style",15),bg="lightyellow").place(x=190,y=90,width=180)

        #==== Row2 =======#

        lbl_tname=Label(self.root,text="Teacher's Name",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=150)
        txt_tname=Entry(self.root,textvariable=self.var_teachername,font=("goudy old style",15),bg="lightyellow").place(x=190,y=150,width=180)
        
        #==== Row3 =======#

        lbl_note=Label(self.root,text="Note",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=210)
        self.txt_note=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_note.place(x=190,y=205,width=210,height=70)

        #========= Buttons ======#
        btn_save=Button(self.root,command=self.add,text="Save",font=("Arial",15),bg="#3b4fd1",fg="white",cursor="hand2").place(x=39,y=365,width=100,height=30)
        btn_update=Button(self.root,command=self.Update,text="Update",font=("Arial",15),bg="#0a7027",fg="white",cursor="hand2").place(x=144,y=365,width=100,height=30)
        btn_delete=Button(self.root,command=self.Delete,text="Delete",font=("Arial",15),bg="#e3292f",fg="white",cursor="hand2").place(x=247,y=365,width=100,height=30)
        btn_clear=Button(self.root,command=self.clear,text="Clear",font=("Arial",15),bg="#524f4f",fg="white",cursor="hand2").place(x=350,y=365,width=100,height=30)

         #===== Time Table Details =========#
        #------- Making Database Table --------#

        std_Frame=Frame(self.root,bd=3,relief=GROOVE,bg="white")
        std_Frame.place(x=500,y=80,width=520,height=340)

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

#-------- ADD BUTTON FUNCTION -------#

    def add(self):
          con=sqlite3.connect(database=r'std_query.db')
          cur=con.cursor()
          try:
            if self.var_date.get()=="":
              messagebox.showerror("Error"," Date must be required",parent=self.root)
            else:
              cur.execute("select* from std_note where date=?",(self.var_date.get(),))
              row=cur.fetchone()
              if row != None:
                  messagebox.showerror("Error","This Date already assigned,try diffrent",parent=self.root)
              else:
                  cur.execute("Insert into std_note(date,teachername,note)values(?,?,?)",(
                                            self.var_date.get(),
                                            self.var_teachername.get(),
                                            self.txt_note.get('1.0',END),
                                          
                ))
                  con.commit()
                  messagebox.showinfo("Success","Note Added Successfully",parent=self.root)
                  self.show()
          except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


  #----------- SHOW DATA IN DATABASE TABLE ------------#

    def show(self):
      con=sqlite3.connect(database=r'std_query.db')
      cur=con.cursor()
      try:
        cur.execute("select * from std_note")
        rows=cur.fetchall()
        self.admin_note_table.delete(*self.admin_note_table.get_children())
        for row in rows:
          self.admin_note_table.insert('',END,values=row)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  #---------- DATA VIEW ---------------#

    def get_data(self,ev):
      f=self.admin_note_table.focus()
      content=(self.admin_note_table.item(f))
      row=content['values']
  
      self.var_date.set(row[0]),
      self.var_teachername.set(row[1]),
      self.txt_note.delete('1.0',END),
      self.txt_note.insert(END,row[2])
    
  
  #----------- UPDATE BUTTON FUNCTION -------------------#

    def Update(self):
      con=sqlite3.connect(database=r'std_query.db')
      cur=con.cursor()
      try:
        if self.var_date.get()=="":
          messagebox.showerror("Error","Date must be required",parent=self.root)
        else:
          cur.execute("select * from std_note where date=?",(self.var_date.get(),))
          row=cur.fetchone()
          if row == None:
            messagebox.showerror("Error","Invalid.....",parent=self.root)
          else:
            cur.execute("update std_note set teachername=?,note=? where date=?",(
                                        self.var_date.get(),
                                        self.var_teachername.get(),
                                        self.txt_note.get('1.0',END),
                                        
            ))
            con.commit()
            messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
            self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  #----------- DELETE BUTTON FUNCTION ------------------#

    def Delete(self):
        con=sqlite3.connect(database=r'std_query.db')
        cur=con.cursor()
        try:
          if self.var_date.get()=="":
            messagebox.showerror("Error","Date must be required",parent=self.root)
          else:
            cur.execute("select * from std_note where date=? ",(self.var_date.get(),))
            row=cur.fetchone()
            if row == None:
              messagebox.showerror("Error","Invalid Roll No",parent=self.root)
            else:
              op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
              if op==True:
                cur.execute("delete  from std_note where date=? ",(self.var_date.get(),))
                con.commit()
                messagebox.showinfo("Delete","Note Deleted Successfully",parent=self.root)
                self.clear()

        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    #--------- CLEAR BUTTON FUNCTION -------------#    

    def clear(self):
      self.var_date.set(""),
      self.var_teachername.set(""),
      self.txt_note.delete('1.0',END),
      self.show()



if __name__=="__main__":
  root=Tk()
  obj=adminnoteclass(root)
  root.mainloop()


  #----UPDATE BUTTON PROBLEM------










  '''
  #---------- SEARCH BUTTON FUNCTION ----------------------
    def search(self):
      con=sqlite3.connect(database=r''std_query.db')
      cur=con.cursor()
      try:
        if self.var_searchby.get()=="Select":
          messagebox.showerror("Error","Select Search By option",parent=self.root)
        elif self.var_searchtxt.get()=="":
          messagebox.showerror("Error","Search Input should be required",parent=self.root)
        else:
          cur.execute("select * from Registration_Table where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")  #.. Its the search quary....
          rows=cur.fetchall()
          if len(rows)!=0:
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
              self.studentTable.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found",parent=self.root)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  '''