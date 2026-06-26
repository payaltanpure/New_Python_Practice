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
sid= int(input("Enter yr id:\n"))
sname= input("Enter yr name:\n")
age= int(input("Enter yr age:\n"))


cursor.execute("insert into stud(sid, sname, age) values (?,?,?)", (sid, sname, age));
conn.commit()
print("Record 2 Inserted")

#update 
cursor.execute("update stud set sname='Shiv' where sid= 1");
