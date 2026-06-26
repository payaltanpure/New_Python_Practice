import sqlite3

conn=sqlite3.connect("student.db")

cursor= conn.cursor()

cursor.execute(""" 
create table stud (
                sid integer pimary key,
                sname text not null,
               age integer check(age>5 & age)
               )
""")

