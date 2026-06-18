# lambda with map function
num=[1,2,3]
op=list(map(lambda no: no*no, num))
print(op)


# task
# print the sqaures of list ele and store output in list again
prices=[100,200,300,400,500]

op= list(map(lambda no: no +(no*0.1), prices))
print(op)



# here there is no need of list becoz we want to conveert the output into list like above 2 eample swe have 
# to cal sum of list ele so ans will be only one number so we used sum function outside and do sum of all nos by calling one by one no from the list into no variable and then store in op 
prices=[10,20,30,40,50]
op= sum(map(lambda no: no, prices))
print(op)


# lambda with filter function

nums=[1,2,3,4,5]

op= list(filter(lambda no: no%2==0, nums)
print(op)