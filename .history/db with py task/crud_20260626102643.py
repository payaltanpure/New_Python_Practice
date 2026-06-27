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
    id = int(input("Enter employee id: "))
    new_name = input("Enter new name: ")
    new_sal = int(input("Enter new salary: "))

    cursor.execute(
        "UPDATE emp SET name=?, sal=? WHERE eid=?",
        (new_name, new_sal, id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee Updated")
    else:
        print("Employee Not Found")
    
#search
def search_by_id():
    id= int(input("Enter id to search data:"))
    cursor.execute("select * from emp where eid =? ", id)
    rows= cursor.fetchall()
    print(rows)
    print("Data fetched by id")

def search_by_name():
    name=input("Enter name to search data:")
    cursor.execute("select * from emp where name = ", name)
    rows= cursor.fetchall()
    print(rows)
    print("Data fetched by name")

#delete 
def delete_emp():
    id= int(input("Enter id to delete data:"))
    cursor.execute("delete * from emp where eid =", id)
    print("EMp deleted by id")



#total sal
def total_sal():
    total_sal=0
    cursor.execute("select * from emp ")
    rows= cursor.fetchall()
    for row in rows:
        total_sal+= row[0]
    print("Total salary paid to emp is:", total_sal)

#count_emp
def count_emp():
    count=0
    cursor.execute("select * from emp ")
    rows= cursor.fetchall()
    for row in rows:
        count+=1
    print("Total emp in company are:", count)
