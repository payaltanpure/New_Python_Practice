# def greet():
#     print ("function with no return type and no argument")

# greet()

# def getno(nu m):
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


# user input

# def mul(a,b):
#     return a*b

# a= int(input("Enter no 1:"))
# b= int(input("Enter no 2:"))
# print(mul(a,b))




# types of keyword argument function


# 1. default argument function
# if parameter not passed in fnction calling default value is set as 10 in function defination
# def add(a=0,b=0):
#     return a+b

# print(add())

# 2. positional argument function
# def user (name , age ,city):
#     print("My name is", name, "and age is ",age, "and city is", city)

# user(78,"Ram","Pune")
# user(age=78, name= "Ram", city="Pune")


# 3. arbitary argument function / variable length function

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


#4. keyword arbitary arguument length: to store the data in key value format like dictionary
# def student(**data):
#     print(data)

# student(name="Payal", age=20, city="Pune")

# #5. lambda function/ anonymous function: no name to function given 

# op= lambda num : num*num
# print(op(5))

# op= lambda num1, num2: num1+num2
# print(op(10,20))


#normal function is used when we want to write many lines of code in it but lambda func is used when we 
# want to perform only one line task 






