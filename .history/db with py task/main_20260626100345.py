import crud as c
from db import conn,cursor
from emp import emp

print("Employee Management Syatem")


while True:
    print("1.Add")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("")
    print("5.Exit")
    
    choice= int(input("ENter yr choice:"))

    match choice:
        case 1:
            c.add_emp()
        case 2:
            c.view_emp()
        case 3:
            c.update_emp()
        case 4:
            # c.delete_emp()
            pass
        case 5:
            print("Thankyou!!\nExit")
            # break; not works in match case workd in if else blocks 
            exit()
        case _ :
            print("Invalid choice!")
            



