from emp import emp
from db import conn, cursor

#insert

def add_emp():
    name = input("ENter yr name:")
    sal= int(input("ENter yr salary:"))
    e= emp(name,sal)
    cursor.execute("insert into emp(name, sal) values (?,?)", (e.name, e))