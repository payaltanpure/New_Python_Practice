import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
print("Connected")


cursor= conn

#product add
def add_prod():
    pname= input("Enter product name:")
    price= float(input("Enter product price:"))
    cursor.execute