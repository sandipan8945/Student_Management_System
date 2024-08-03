import sqlite3
def creat_nothing():
    con=sqlite3.connect(database=r'nothing.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Test_TimeTable(day text ,time text ,sub text ,teacherName text)")
    con.commit()

creat_nothing()

