#from ast import Delete
from tkinter import*
from tkinter import ttk,messagebox
#from PIL import Image,ImageTk
import sqlite3

class registrationclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x500+212+130")
        self.root.title("Student Management System | Developed by Sandipan")
        self.root.config(bg="white")
        self.root.focus_force()

        #================================================================#
        #======= ALL VARIABLES ========#
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_regno=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_contact_no=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
      
        
        

        #------ SEARCH FREAME------------------
        searchFrame=LabelFrame(self.root,text="Search Student",font=("goudy old style",12,"bold"),bg="white")
        searchFrame.place(x=250,y=20,width=600,height=70)

        #------Options------
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Name","Rollno","Contact","Email"),state='readonly',justify=CENTER,font=("goudy old",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("Arial",15),bg="crimson",fg="white",cursor="hand2").place(x=430,y=8,width=150,height=30)

        #==== TITLE =====

        title=Label(self.root,text="Student Details",font=("goudy old style",15),relief=GROOVE,bg="#0f4d7d",fg="white").place(x=35,y=100,width=980)

        #--------CONTENT--------------#
        #======= Row1 =======#
        lbl_roll_no=Label(self.root,text="Roll No.",font=("goudy old style",15),bg="white").place(x=39,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=360,y=150)
        lbl_regno=Label(self.root,text="Registration No.",font=("goudy old style",15),bg="white").place(x=675,y=150)

        txt_roll_no=Entry(self.root,textvariable=self.var_roll_no,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)

        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old",15))
        cmb_gender.place(x=460,y=150,width=180)
        cmb_gender.current(0)

        txt_regno=Entry(self.root,textvariable=self.var_regno,font=("goudy old style",15),bg="lightyellow").place(x=825,y=150,width=180)

        #==== Row2 =======#

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=39,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=360,y=190)
        lbl_contact_no=Label(self.root,text="Contact No.",font=("goudy old style",15),bg="white").place(x=675,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=460,y=190,width=180)
        txt_contact_no=Entry(self.root,textvariable=self.var_contact_no,font=("goudy old style",15),bg="lightyellow").place(x=825,y=190,width=180)

        #==== Row3 =======#

        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=39,y=230)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=360,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=675,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=460,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","User"),state='readonly',justify=CENTER,font=("goudy old",15))
        cmb_utype.place(x=825,y=230,width=180)
        cmb_utype.current(0)

        #======= Row4 =======#
        lbl_Address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=39,y=270)
      
        self.txt_Address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_Address.place(x=150,y=270,width=300,height=60)

        #========= Buttons ======#

        btn_save=Button(self.root,text="Save",command=self.add,font=("Arial",15),bg="#3b4fd1",fg="white",cursor="hand2").place(x=520,y=300,width=100,height=30)
        btn_update=Button(self.root,text="Update",comman=self.Update,font=("Arial",15),bg="#0a7027",fg="white",cursor="hand2").place(x=640,y=300,width=100,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.Delete,font=("Arial",15),bg="#e3292f",fg="white",cursor="hand2").place(x=760,y=300,width=100,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Arial",15),bg="#524f4f",fg="white",cursor="hand2").place(x=880,y=300,width=100,height=30)

        #===== Student Details =========#
        #------- Making Database Table --------#


        std_Frame=Frame(self.root,bd=3,relief=GROOVE)
        std_Frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(std_Frame,orient=VERTICAL)
        scrollx=Scrollbar(std_Frame,orient=HORIZONTAL)

        self.studentTable=ttk.Treeview(std_Frame,columns=("rollno","regno","name","gender","dob","contact","email","address","utype","pass"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.studentTable.xview)

        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.studentTable.yview)


        self.studentTable.heading("rollno",text="Roll No")
        self.studentTable.heading("regno",text="Registration No")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("dob",text="D.O.B")
        self.studentTable.heading("contact",text="Contact No")
        self.studentTable.heading("email",text="Email")
        self.studentTable.heading("address",text="Address")
        self.studentTable.heading("utype",text="User Type")
        self.studentTable.heading("pass",text="Password")
        
       

        self.studentTable["show"]='headings' # delete the default blank cell

        self.studentTable.pack(fill=BOTH,expand=1)

        self.studentTable.column("rollno",width=100)
        self.studentTable.column("regno",width=110)
        self.studentTable.column("name",width=110)
        self.studentTable.column("gender",width=110)
        self.studentTable.column("dob",width=110)
        self.studentTable.column("contact",width=110)
        self.studentTable.column("email",width=210)
        self.studentTable.column("address",width=170)
        self.studentTable.column("utype",width=110)
        self.studentTable.column("pass",width=110)
        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===========================================================================#
#======================= DATABASE CONNECTION ================================#

#-------- ADD BUTTON FUNCTION -------#

    def add(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_roll_no.get()=="":
          messagebox.showerror("Error","Roll No must be required",parent=self.root)
        else:
          cur.execute("select* from Registration_Table where rollno=?",(self.var_roll_no.get(),))
          row=cur.fetchone()
          if row != None:
            messagebox.showerror("Error","This Roll No already assigned,try diffrent",parent=self.root)
          else:
            cur.execute("Insert into Registration_Table(rollno,gender,regno,name,dob,contact,email,pass,utype,address)values(?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_roll_no.get(),
                                        self.var_gender.get(),
                                        self.var_regno.get(),
                                        self.var_name.get(),
                                        self.var_dob.get(),
                                        self.var_contact_no.get(),
                                        self.var_email.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_Address.get('1.0',END)
            ))
            con.commit()
            messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
            self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #----------- Show Data in Database Table ------------

    def show(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        cur.execute("select * from Registration_Table")
        rows=cur.fetchall()
        self.studentTable.delete(*self.studentTable.get_children())
        for row in rows:
          self.studentTable.insert('',END,values=row)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  #---------- Data View ---------------

    def get_data(self,ev):
      f=self.studentTable.focus()
      content=(self.studentTable.item(f))
      row=content['values']
  
      self.var_roll_no.set(row[0]),
      self.var_regno.set(row[1]),
      self.var_name.set(row[2]),
      self.var_gender.set(row[3]),
      self.var_dob.set(row[4]),
      self.var_contact_no.set(row[5]),
      self.var_email.set(row[6]),
      self.txt_Address.delete('1.0',END),
      self.txt_Address.insert(END,row[7])
      self.var_utype.set(row[8]),
      self.var_pass.set(row[9]),
      
      
      
  #----------- UPDATE BUTTON FUNCTION -------------------

    def Update(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_roll_no.get()=="":
          messagebox.showerror("Error","Roll No must be required",parent=self.root)
        else:
          cur.execute("select* from Registration_Table where rollno=?",(self.var_roll_no.get(),))
          row=cur.fetchone()
          if row == None:
            messagebox.showerror("Error","Invalid Roll No",parent=self.root)
          else:
            cur.execute("update Registration_Table set regno=?,name=?,gender=?,dob=?,contact=?,email=?,address=?,utype=?,pass=? where rollno=?",(
                                        self.var_regno.get(),
                                        self.var_name.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_contact_no.get(),
                                        self.var_email.get(),
                                        self.txt_Address.get('1.0',END),
                                        self.var_utype.get(),
                                        self.var_pass.get(),
                                        self.var_roll_no.get()
            ))
            con.commit()
            messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
            self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  #----------- DELETE BUTTON FUNCTION ------------------
    def Delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
          if self.var_roll_no.get()=="":
            messagebox.showerror("Error","Roll No must be required",parent=self.root)
          else:
            cur.execute("select * from Registration_Table where rollno=? ",(self.var_roll_no.get(),))
            row=cur.fetchone()
            if row == None:
              messagebox.showerror("Error","Invalid Roll No",parent=self.root)
            else:
              op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
              if op==True:
                cur.execute("delete  from Registration_Table where rollno=? ",(self.var_roll_no.get(),))
                con.commit()
                messagebox.showinfo("Delete","Student Details Deleted Successfully",parent=self.root)
                self.clear()

        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


     #--------- CLEAR BUTTON FUNCTION -------------     

    def clear(self):
      self.var_roll_no.set(""),
      self.var_regno.set(""),
      self.var_name.set(""),
      self.var_gender.set("Select"),
      self.var_dob.set(""),
      self.var_contact_no.set(""),
      self.var_email.set(""),
      self.txt_Address.delete('1.0',END),
      self.var_utype.set("Select"),
      self.var_pass.set(""),
      self.var_searchtxt.set("")
      self.var_searchby.set("Select")
      self.show()


  #---------- SEARCH BUTTON FUNCTION ----------------------
    def search(self):
      con=sqlite3.connect(database=r'sms.db')
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



if __name__=="__main__":
  root=Tk()
  obj=registrationclass(root)
  root.mainloop()
