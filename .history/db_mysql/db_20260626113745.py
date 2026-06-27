import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
print("Connected")


cursor= conn.cursor()

# #product add
# def add_prod():
#     pname= input("Enter product name:")
#     price= float(input("Enter product price:"))
#     cursor.execute("insert into product (pname,price) values (%s, %s)", (pname, price))
#     conn.commit()
#     print("Data inserted")

# add_prod()


#view product
# def view_prod():
#     cursor.execute("select * from product")
#     rows= cursor.fetchall()
#     print(rows)
#     print("Product fetched")

#     for row in rows:
#         print(row[0], row[1] ,row[2] )
    
# view_prod()

#add customer data

# def add_cust():
#     cname=input("Enter customer name:")
#     add=input("Enter customer address:")
#     pid= int(input("Enter product id:"))
#     cursor.execute("insert into customer (cname, address, pid) values (%s, %s , %s)", (cname,add,pid))
#     conn.commit()
#     print("Customer added")

# add_cust()

# #view customer
# def view_cust():
#         cursor.execute("select * from customer")
#         rows= cursor.fetchall()
#         print(rows)
#         print("Customer fetched")

#         for row in rows:
#             print(row[0], row[1] ,row[2], row[3] )

# view_cust()

#use joins to fetch data from both tables at a time which are related  to each other 

#payal buys pid 1 that is car

def joins():
    cursor.execute("""
        SELECT c.cname, c.address, p.pname, p.price
        FROM customer AS c
        JOIN product AS p
        ON c.pid = p.pid
    """)
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print("Data from both tables fetched")

joins()


def joins2():
    cursor.execute("""
        SELECT c.cname, c.address, p.pname, p.price
        FROM customer c
        JOIN product p
        ON c.pid = p.pid
    """)

    rows = cursor.fetchall()

    for row in rows:
        print(f"Customer Name : {row[0]}")
        print(f"Address       : {row[1]}")
        print(f"Product Name  : {row[2]}")
        print(f"Price         : {float(row[3])}")
        print("-" * 30)

    print("Data from both tables fetched.")