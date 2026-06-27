import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
print("Connected")


cursor= conn.cursor()

#product add
def add_prod():
    pname= input("Enter product name:")
    price= float(input("Enter product price:"))
    cursor.execute("insert into product (pname,price) values (%s, %s)", (pname, price))
    conn.commit()
    print("Data inserted")