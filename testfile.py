import sqlite3
def creat_database():
    con=sqlite3.connect(database=r'test_file.db')
    cur=con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS Admin_TimeTable(day text ,time text ,sub text ,TeacherName text)")
    con.commit()

creat_database()