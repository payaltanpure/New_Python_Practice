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

list=[]
no = int(input(("How many values do you want")))
while(no!=0):
        a= int(input("Enter value for no"))
        list.append(a)
        no=no-1

def add(*args):
        sum=0
        for i in args:
            sum+=i
        return sum
op= add(list)















