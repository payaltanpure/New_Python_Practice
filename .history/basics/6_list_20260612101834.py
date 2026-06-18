# x= [10,20,30,40,77,99]

# sum=0
# even=0
# for ch in x:
#     sum+=ch
#     if ch%2==0:
#        even+=ch
# print("Sum of list ele is :", sum)
# print("Even ele sum is:", even)

# x= [10,20,30,40,77,99]
# max=0
# print(x[2])

# for i in x:
#     if i>max:
#         max= i
# print("Max element:", max)


# when we use range in for loop var of for loop refers index of list and when we not use range it refers to value of list 

# x= [10,20,30,40,77,99]
# for i in range(len(x)): 
#     # len(x)= 6 passes start 0-end 5 and step by default 1 range to range function and returns one one index to i in for loop
#     if x[i]==30:
#         x[i]=0
# print(x)

# x=[20,30,40]
# rev=[]
# for i in range(len(x)-1, -1,-1): 
#     # start= len(x)-1= 3-1=2 index , end = -1 , step=-1
#     rev.append(x[i])
# print(rev)


# x=[20,30,40,30,20,10,44,55]
# y=[]
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)

x=[20,30,40,30,20,10,44,55]