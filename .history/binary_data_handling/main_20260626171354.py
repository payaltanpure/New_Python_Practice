import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
print("Connected")


cursor= conn.cursor()

cursor.execute(""" 
create table if not exists (
               sid int primary key not null autoincrement,
               san)""")