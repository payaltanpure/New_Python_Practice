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

# types of keyword argument function


# 1. default argument function
# if parameter not passed in fnction calling default value is set as 10 in function defination
# def add(a=0,b=0):
#     return a+b

# print(add())

# 2. positional argument function
def user (name , age ,city):
    print("My name is", name, "and age is ",age, "and city is", city)


user(age=78, name= "Ram", city="Pune")



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


# Definition:
# Passing values from one function to another means transferring the output produced by one function so that it can be used as input by another function.

# Method
# The first function performs a task and returns a value using the return statement.
# The returned value is stored in a variable or directly passed as an argument.
# The second function receives this value through its parameter and uses it for further processing.
# Flow
# Function 1
#     ↓ (return value)
# Variable
#     ↓ (argument)
# Function 2
# Example
# def percentage(total):
#     return (total/500)*100

# def grade(per):
#     if per >= 75:
#         return "A"

# per = percentage(400)
# g = grade(per)
# Theory Answer for Exam

# Values are passed from one function to another using the return statement and function arguments. The first function returns the required value after processing. This returned value is stored in a variable or directly supplied as an argument to another function. The receiving function accepts the value through its parameters and performs further operations on it. This technique improves modularity, code reusability, and communication between functions.

# In Your Student Program
# get_marks()
#       ↓ returns total
# calculate_percentage(total)
#       ↓ returns percentage
# calculate_grade(percentage)
#       ↓ returns grade
# Display Result






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

# Good observation.

# In Python, variables created inside a case block are actually 
# available outside the block because Python does not create a new scope for match-case.

# For example:

# match choice:
#     case 2:
#         per = calculate_percentage(total, n)
#         print(per)

#     case 3:
#         print(per)

# This will work only if Case 2 was executed before Case 3.

# The problem is:

# User selects 3 directly

# then per has never been created, so Python gives:

# NameError: name 'per' is not defined

# That's why in my code I recalculated percentage in Case 3:

# case 3:
#     per = calculate_percentage(total, n)
#     grade = calculate_grade(per)