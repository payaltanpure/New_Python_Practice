# lambda with map function
num=[1,2,3]
op=list(map(lambda no: no*no, num))
print(op)

# without using list output will be like this <map object at 0x00000243EAAABAF0> becoz output has many no as a result

# task
# print the sqaures of list ele and store output in list again
prices=[100,200,300,400,500]

op= list(map(lambda no: no +(no*0.1), prices))
print(op)


# and without using list output will be like this <map object at 0x00000243EAAABAF0> becoz output has many no as a result so we used list in above example but below we use sum function so ans is only one so we do not used list 
# here there is no need of list becoz we want to conveert the output into list like above 2 eample so have 
# to cal sum of list ele so ans will be only one number so we used sum function outside and do sum of all nos by calling one by one no from the list into no variable and then store in op 
prices=[10,20,30,40,50]
op= sum(map(lambda no: no, prices))
print(op)


# lambda with filter function

nums=[1,2,3,4,5]

op= list(filter(lambda no: no%2==0, nums))
print(op)


sal= [1000,2000,5500,7000]

op=  list()