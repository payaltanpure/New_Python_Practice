import crud
from db import conn,cursor
from emp import *

print("Employee Management Syatem")


while True:
    print("1.Add")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")
    
    choice= int(input("ENter yr choice:"))

    match choice:
        case 1:
            crud.add_emp()
