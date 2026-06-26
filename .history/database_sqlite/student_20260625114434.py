import sqlite3

conn=sqlite3.connect("student.db")

cursor= conn.cursor()

# cursor.execute(""" 
# create table stud (
#                 sid integer pimary key,
#                 sname text not null,
#                 age integer check(age>5 & age<18)
#                )
# """)

conn.commit()
print("Database and table is created")


#insert data
cursor.execute("insert into stud(sid, sname, age) values (?,?,?)", (1,"Payal",21));
conn.commit()
print("Record 1 Inserted")


#user input
sid= int(input())
cursor.execute("insert into stud(sid, sname, age) values (?,?,?)", (1,"Payal",21));
conn.commit()
print("Record Inserted")