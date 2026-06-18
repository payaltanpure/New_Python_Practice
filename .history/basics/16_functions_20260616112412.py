# def greet():
#     print ("function with no return type and no argument")

# greet()

# def getno(num):
#     print("No is :",num)

# getno(2)

# def get_sq():
#     return 2*2

# op=get_sq()
# print(op*2)
# print(get_sq())


# def add(a,b):
#     return a+b

# print(add(10,20))
# op= add(20,30)
# print(op**2)


# def add(*args):
#      total= sum(args)
#      return total
# print(add(10,20,30,40,50))

# # drawback of normal function is overcomed as in normal functions we have to write diff code for diff no of arguments , as out reqiremnet changes we have to build new function with req no of arguments
# # this allows us to pass as many req parameters to the function without any declaration of that variable in function 


# def add(*args):
#      sum=0
#      for i in args:
#        sum+=i
#      return sum
# print(add(10,20,30,40,50))
# op= add(1,2,3,4,5)
# print(op)


# def mul(a,b):
#     return a*b

# a= int(input("Enter no 1:"))
# b= int(input("Enter no 2:"))
# print(mul(a,b))



# # taking multiple user input as per req and pass to function to add using *args 
# lst = []
# no = int(input("How many values do you want: "))

# while no != 0:
#     a = int(input("Enter value: "))
#     lst.append(a)
#     no -= 1

# def add(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# op = add(*lst)      # Unpacking list
# # add(*lst) becomes:
# # add(10, 20, 30)
# print(op)


# i is [10, 20, 30] (a list), so Python tries:
# 0 + [10,20,30]
# so error above is the solution of unpacking the list and pass the list ele normally as parameters 


def get_marks():
    name = input("Enter Student Name: ")
    n = int(input("Enter Number of Subjects: "))

    total = 0
    for i in range(1, n + 1):
        mark = int(input(f"Enter Marks of Subject {i}: "))
        total += mark

    return name, total, n


def calculate_percentage(total, n):
    return (total / (n * 100)) * 100


def calculate_grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"


name = ""
total = 0
n = 0

while True:
    print("\n----- MENU -----")
    print("1. Enter Student Details")
    print("2. Calculate Percentage")
    print("3. Display Grade")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    match choice:
        case 1:
            name, total, n = get_marks()

        case 2:
            if n == 0:
                print("Enter student details first!")
            else:
                per = calculate_percentage(total, n)
                print("Percentage =", per)

        case 3:
            if n == 0:
                print("Enter student details first!")
            else:
                per = calculate_percentage(total, n)
                grade = calculate_grade(per)

                print("\nName:", name)
                print("Total Marks:", total)
                print("Percentage:", per)
                print("Grade:", grade)

        case 4:
            print("Program Ended")
            break

        case _:
            print("Invalid Choice")

Good observation.

In Python, variables created inside a case block are actually 
available outside the block because Python does not create a new scope for match-case.