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
create table if not exists stud  (
               sid int primary key not null auto_increment,
               sname varchar(20) not null,
               stud_photo varchar(20),
               photo_data LONGBLOB )""")

conn.commit()

print("Table created!")

with open("binary_data_handling/image.png", "rb") as file :
    binary_data= file.read()
print("Data fetched!")


#insert 
cursor.execute("insert into stud(sname, stud_photo, photo_data) values(%s, %s, %s)", )
