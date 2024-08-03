from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class admintimetableclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()   # focus_force is use for focus the edge of the tab

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_day=StringVar()
        self.var_time=StringVar()
        self.var_sub=StringVar()
        self.var_tname=StringVar()
  

        #------ SEARCH FREAME------------------
        searchFrame=LabelFrame(self.root,text="Search Days",font=("goudy old style",12,"bold"),bg="white")
        searchFrame.place(x=550,y=60,width=450,height=70)
      
       #------Options------
        txt_search=Label(searchFrame,text="Days",font=("goudy old",15),bg="white").place(x=20,y=6)
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"),state='readonly',justify=CENTER,font=("goudy old",15))
        cmb_search.place(x=95,y=6,width=180)
        cmb_search.current(0)

        
        btn_search=Button(searchFrame,command=self.search,text="Search",font=("Arial",15),bg="crimson",fg="white",cursor="hand2").place(x=290,y=5,width=150,height=30)

        #==== TITLE =====

        title=Label(self.root,text="Time Table",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=20,width=980)

        #--------CONTENT--------------#

        #======= Row1 =======#
        lbl_day=Label(self.root,text="Days",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=100)
        txt_day=ttk.Combobox(self.root,textvariable=self.var_day,values=("Select","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"),state='readonly',justify=CENTER,font=("goudy old",15)).place(x=190,y=100,width=180)

        #==== Row2 =======#

        lbl_time=Label(self.root,text="Time",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=160)
        txt_time=Entry(self.root,textvariable=self.var_time,font=("goudy old style",15),bg="lightyellow").place(x=190,y=160,width=180)
        
        #==== Row3 =======#

        lbl_sub=Label(self.root,text="Subject",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=210)
        txt_sub=Entry(self.root,textvariable=self.var_sub,font=("goudy old style",15),bg="lightyellow").place(x=190,y=210,width=250,height=50)

        #==== Row4 =======#

        lbl_tname=Label(self.root,text="Teacher's Name",font=("goudy old style",15,"bold"),bg="white").place(x=39,y=280)
        txt_tname=Entry(self.root,textvariable=self.var_tname,font=("goudy old style",15),bg="lightyellow").place(x=190,y=280,width=180)
  
        #========= Buttons ======#

        btn_save=Button(self.root,text="Save",command=self.add,font=("Arial",15),bg="#3b4fd1",fg="white",cursor="hand2").place(x=39,y=400,width=100,height=30)
        btn_update=Button(self.root,text="Update",command=self.Update,font=("Arial",15),bg="#0a7027",fg="white",cursor="hand2").place(x=140,y=400,width=100,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.Delete,font=("Arial",15),bg="#e3292f",fg="white",cursor="hand2").place(x=242,y=400,width=100,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Arial",15),bg="#524f4f",fg="white",cursor="hand2").place(x=343,y=400,width=100,height=30)

        #===== Time Table Details =========#
        #------- Making Database Table --------#


        std_Frame=Frame(self.root,bd=3,relief=GROOVE,bg="white")
        std_Frame.place(x=500,y=150,width=540,height=310)

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
        #self.timetable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#===========================================================================#
#======================= DATABASE CONNECTION ================================#

#-------- ADD BUTTON FUNCTION -------#

    def add(self):
      con=sqlite3.connect(database=r'nothing.db')
      cur=con.cursor()
      try:
        if self.var_day.get()=="Select":
          messagebox.showerror("Error","Day must be required",parent=self.root)
        else:
          cur.execute("select* from Test_TimeTable where day=?",(self.var_day.get(),))
          row=cur.fetchone()
          if row == None:
            messagebox.showerror("Error","Invalid input, Try something",parent=self.root)
          else:
            cur.execute("Insert into Test_TimeTable(day,time,sub,teacherName)values(?,?,?,?)",(
                                        self.var_day.get(),
                                        self.var_time.get(),
                                        self.var_sub.get(),
                                        self.var_tname.get(),
                                        
                                        
            ))
            con.commit()
            messagebox.showinfo("Success","Time Table added Successfully",parent=self.root)
            self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

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


    
  #----------- UPDATE BUTTON FUNCTION -------------------

    def Update(self):
      con=sqlite3.connect(database=r'nothing.db')
      cur=con.cursor()
      try:
        if self.var_day.get()=="" and self.var_sub.get()=="":
          messagebox.showerror("Error","Select any option",parent=self.root)
        else:
          cur.execute("select * from Test_TimeTable where day=? AND sub=?",(self.var_day.get(),self.var_sub.get(),))
          row=cur.fetchone()
          #if row == None:
            #messagebox.showerror("Error","Invalid.....",parent=self.root)
          #else:
          cur.execute("update Test_TimeTable set time=?,sub=?,teacherName=? where day=?",(
                                        
                                        self.var_time.get(),
                                        self.var_sub.get(),
                                        self.var_tname.get(),
                                        self.var_day.get(),
                                        
            ))
          con.commit()
          messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
          self.show()
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


  #----------- DELETE BUTTON FUNCTION ------------------
    def Delete(self):
        con=sqlite3.connect(database=r'nothing.db')
        cur=con.cursor()
        try:
          if self.var_day.get()=="":
            messagebox.showerror("Error","Day must be required",parent=self.root)
          else:
            cur.execute("select* from Test_TimeTable where day=?",(self.var_day.get(),))
            row=cur.fetchone()
            if row == None:
              messagebox.showerror("Error","This date is not here,choose the right date",parent=self.root)
            else:
              op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
              if op==True:
                cur.execute("delete from Test_TimeTable where day=?",(self.var_day.get(),))
                con.commit()
                messagebox.showinfo("Delete","Time Schdule Details Deleted Successfully",parent=self.root)
                self.clear()

        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
     #--------- CLEAR BUTTON FUNCTION -------------     

    def clear(self):
      self.var_day.set("Select"),
      self.var_time.set(""),
      self.var_tname.set(""),
      self.var_sub.set(""),
      self.var_searchby.set("Select")
      self.show()


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
  obj=admintimetableclass(root)
  root.mainloop()


  '''
  ----PROBLEMS---
  Update button problem
  delete button
  search button

  when i select one option than it fetch all 
  '''