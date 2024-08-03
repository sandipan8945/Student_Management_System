import sqlite3
def creat_database():
    con=sqlite3.connect(database=r'sms.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Registration_Table(rollno INTEGER PRIMARY KEY AUTOINCREMENT ,regno text ,name text ,gender text ,dob text ,contact text ,email text ,address text ,utype text ,pass text)")
    con.commit()

creat_database()