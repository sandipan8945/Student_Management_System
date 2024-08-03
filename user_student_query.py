from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class userqueryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====variable=======
        self.var_date=StringVar()
        self.var_studentname=StringVar()
        self.txt_query=StringVar()

        title=Label(self.root,text="Student's Query",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=20,width=980)

        #========Images=======
        self.background=ImageTk.PhotoImage(file="images/help6.jpg")
        self.lbl_image=Label(self.root,image=self.background,bg="white").place(x=500,y=50)


        #======= Row1 =======#
        lbl_date=Label(self.root,text="Date",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=100)
        txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style",15),bg="lightyellow").place(x=190,y=100,width=180)

        #==== Row2 =======#

        lbl_studentname=Label(self.root,text="Student's Name",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=160)
        txt_studentname=Entry(self.root,textvariable=self.var_studentname,font=("goudy old style",15),bg="lightyellow").place(x=190,y=160,width=180)
        
        #==== Row3 =======#

        lbl_query=Label(self.root,text="Query",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=220)
        self.txt_query=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_query.place(x=190,y=220,width=250,height=70)

  
        #========= Buttons ======#
        btn_save=Button(self.root,command=self.add,text="Save",font=("Arial",15),bg="#3b4fd1",fg="white",cursor="hand2").place(x=50,y=400,width=100,height=30)
        btn_clear=Button(self.root,command=self.clear,text="Clear",font=("Arial",15),bg="#524f4f",fg="white",cursor="hand2").place(x=170,y=400,width=100,height=30)

        self.timetable=ttk.Treeview(self.root,columns=("date","studentname","query"))

#===========================================================================#
#======================= DATABASE CONNECTION ================================#

#-------- ADD BUTTON FUNCTION -------#

    def add(self):
      con=sqlite3.connect(database=r'std_query.db')
      cur=con.cursor()
      try:
        if self.var_date.get()=="Select":
          messagebox.showerror("Error","Date must be required",parent=self.root)
        else:
          cur.execute("select* from Query_Table where date=?",(self.var_date.get(),))
          row=cur.fetchone()
          
          cur.execute("Insert into Query_Table(date,studentname,query)values(?,?,?)",(
                                        self.var_date.get(),
                                        self.var_studentname.get(),
                                        self.txt_query.get('1.0',END),
                                                                
            ))
          con.commit()
          messagebox.showinfo("Success","Time Table added Successfully",parent=self.root)
          self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

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

     #--------- CLEAR BUTTON FUNCTION -------------     

    def clear(self):
      self.var_date.set("Select"),
      self.var_studentname.set(""),
      self.txt_query.delete('1.0',END),
    
      self.show()




if __name__=="__main__":
  root=Tk()
  obj=userqueryclass(root)
  root.mainloop()




  '''
  #---------- Data View ---------------

    def get_data(self,ev):
      f=self.timetable.focus()
      content=(self.timetable.item(f))
      row=content['values']
  
      self.var_date.set(row[0]),
      self.var_studentname.set(row[1]),
      self.txt_query.delete('1.0',END),
      self.txt_query.insert(END,row[2]),


      
  #----------- DELETE BUTTON FUNCTION ------------------
    def Delete(self):
        con=sqlite3.connect(database=r'std_query.db')
        cur=con.cursor()
        try:
          if self.var_date.get()=="":
            messagebox.showerror("Error","Day must be required",parent=self.root)
          else:
            cur.execute("select* from Query_Table where day=?",(self.var_date.get(),))
            row=cur.fetchone()
            if row == None:
              messagebox.showerror("Error","This date is not here,choose the right date",parent=self.root)
            else:
              op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
              if op==True:
                cur.execute("delete from Query_Table where day=?",(self.var_date.get(),))
                con.commit()
                messagebox.showinfo("Delete","Time Schdule Details Deleted Successfully",parent=self.root)
                self.clear()

        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        '''