import sqlite3
def creat_student():
    con=sqlite3.connect(database=r'std_query.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Query_Table(date text ,studentname text ,query text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS std_note(date text ,teachername text ,note text)")
    con.commit()

creat_student()
