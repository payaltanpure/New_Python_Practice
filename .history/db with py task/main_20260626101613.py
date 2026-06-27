import crud as c
from db import conn,cursor
from emp import emp

print("Employee Management Syatem")


while True:
    print("1.Add")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("5.Search")
    print("6.Exit")
    
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
        case 5:
            print("1.Search by id\n 2. Search by name\n3.Exit")
            ip= int(input("Ebter yr choice"))
            while True:
                if ip==1:
                    c.search_by_id()
                elif ip==2:
                    c.search_by_name()
                elif ip==3:
                    print("Exit")
                    break;
                else:
                    print("Invalid input")

        case 6:
            print("Thankyou!!\nExit")
            # break; not works in match case workd in if else blocks 
            exit()
        case _ :
            print("Invalid choice!")
            



