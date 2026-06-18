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



# def get_marks():
#     name = input("Enter Student Name: ")
#     n = int(input("Enter Number of Subjects: "))

#     total = 0
#     for i in range(1, n + 1):
#         mark = int(input(f"Enter Marks of Subject {i}: "))
#         total += mark

#     return name, total, n


# def calculate_percentage(total, n):
#     return (total / (n * 100)) * 100


# def calculate_grade(per):
#     if per >= 90:
#         return "A"
#     elif per >= 75:
#         return "B"
#     elif per >= 60:
#         return "C"
#     elif per >= 40:
#         return "D"
#     else:
#         return "Fail"


# name = ""
# total = 0
# n = 0

# while True:
#     print("\n----- MENU -----")
#     print("1. Enter Student Details")
#     print("2. Calculate Percentage")
#     print("3. Display Grade")
#     print("4. Exit")

#     choice = int(input("Enter Choice: "))

#     match choice:
#         case 1:
#             name, total, n = get_marks()

#         case 2:
#             if n == 0:
#                 print("Enter student details first!")
#             else:
#                 per = calculate_percentage(total, n)
#                 print("Percentage =", per)

#         case 3:
#             if n == 0:
#                 print("Enter student details first!")
#             else:
#                 per = calculate_percentage(total, n)
#                 grade = calculate_grade(per)

#                 print("\nName:", name)
#                 print("Total Marks:", total)
#                 print("Percentage:", per)
#                 print("Grade:", grade)

#         case 4:
#             print("Program Ended")
#             break

#         case _:
#             print("Invalid Choice")

# # Good observation.

# # In Python, variables created inside a case block are actually 
# # available outside the block because Python does not create a new scope for match-case.

# # For example:

# # match choice:
# #     case 2:
# #         per = calculate_percentage(total, n)
# #         print(per)

# #     case 3:
# #         print(per)

# # This will work only if Case 2 was executed before Case 3.

# # The problem is:

# # User selects 3 directly

# # then per has never been created, so Python gives:

# # NameError: name 'per' is not defined

# # That's why in my code I recalculated percentage in Case 3:

# # case 3:
# #     per = calculate_percentage(total, n)
# #     grade = calculate_grade(per)