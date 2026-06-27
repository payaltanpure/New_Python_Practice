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


photo_name= "image.png"
with open("binary_data_handling/image.png", "rb") as file :
    photo_data= file.read()
print("Data fetched!")


#insert 
cursor.execute("insert into stud(sname, stud_photo, photo_data) values(%s, %s, %s)", ("Payal",photo_name, photo_data))
conn.commit()
print("Image inserted")


#read
cursor.execute("select * from stud where sid=%s", (1,))
row = cursor.fetchone()

print("Fetched")