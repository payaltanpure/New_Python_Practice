from emp import emp
from db import conn, cursor

#insert

def add_emp():
    ip= int(input("How many employee to add:"))
    for i in range(1, ip+1):
        name = input("ENter yr name:")
        sal= int(input("ENter yr salary:"))
        e= emp(name,sal)
        cursor.execute("insert into emp(name, sal) values (?,?)", (e.name, e.sal))
        conn.commit()
        print("Data inserted ")
        print(i, "added")

#read
def view_emp():
    cursor.execute("select * from emp")
    rows= cursor.fetchall()
    print(rows)
    print("Data fetched")


#update
def update_emp():
    id= int(input("Enter id to update data:"))
    new_name = input("ENter yr name:")
    new_sal= int(input("ENter yr salary:"))
    cursor.execute("select * from emp")
    rows= cursor.fetchall()
    for row in rows:
       if (row[0]==id):
           cursor.execute("update emp set name=", new_name)
           cursor.execute("update emp set sal=", new_sal)
           print("Emp updated ")
       else:   
           print("Emp not found!")
    
#search
def search_by_id():
    id= int(input("Enter id to search data:"))
    cursor.execute("select * from emp where id = id")
    rows= cursor.fetchall()



