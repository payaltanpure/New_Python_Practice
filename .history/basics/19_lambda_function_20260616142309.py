# lambda with map function
num=[1,2,3]
op=list(map(lambda no: no*no, num))
print(op)

# task
prices=[100,200,300,400,500]

op= list(map(lambda no: no +(no*0.1), prices))
print(op)



# here there is no need of list becoz we want to conveert the output into list like above 2 eample swe have 
# to cal sum of list ele so ans will be only one 
prices=[10,20,30,40,50]
op= sum(map(lambda no: no, prices))
print(op)