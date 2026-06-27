from emp import emp
import db.py

#insert

def add_emp():
    name = input("ENter yr name:")
    sal= int(input("ENter yr salary:"))
    e= emp(name,sal)
    