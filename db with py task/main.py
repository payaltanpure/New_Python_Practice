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
    print("6.Total Salary")
    print("7.Count total emp")
    print("8.Exit")
    
    choice= int(input("ENter yr choice:"))

    match choice:
        case 1:
            c.add_emp()
        case 2:
            c.view_emp()
        case 3:
            c.update_emp()
        case 4:
            c.delete_emp()
            
        case 5:
           
            while True:
                print("\n------ Search Menu ------")
                print("1. Search by ID")
                print("2. Search by Name")
                print("3. Exit Search")

                ip = int(input("Enter your choice: "))

                match ip:
                    case 1:
                        c.search_by_id()
                    case 2:
                        c.search_by_name()
                    case 3:
                        print("Exiting Search Menu...")
                        break
                    case _:
                        print("Invalid choice! Try again.")
        
        case 6:
            c.total_sal()

        case 7:
            c.count_emp()

        case 8:
            print("Thankyou!!\nExit")
            # break; not works in match case workd in if else blocks 
            exit()
        case _ :
            print("Invalid choice!")
            



