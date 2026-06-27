from emp import emp
from db import conn, cursor

#insert

def add_emp():
    name = input("ENter yr name:")
    sal= int(input("ENter yr salary:"))
    e= emp(name,sal)
    cursor.execute("insert into emp(name, sal) values (?,?)", (e.name, e.sal))
    conn.commit()
    print("Data inserted ")

#read
def view_emp():
    cursor.execute("select * from emp")
    rows= cursor.fetchall()
    print(rows)
    print("Data fetched")


#update
def update_emp()

