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


def add(*args):
     total= sum(args)
     return total
print(add(10,20,30,40,50))

# drawback of 
# this allows us to pass as many req parameters to the function without any declaration of that variable in function 