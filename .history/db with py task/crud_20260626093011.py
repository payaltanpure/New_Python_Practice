from emp import emp
from db.py import c

#insert

def add_emp():
    name = input("ENter yr name:")
    sal= int(input("ENter yr salary:"))
    e= emp(name,sal)
    