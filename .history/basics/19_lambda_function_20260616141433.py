# lambda with map function
num=[1,2,3]
op=list(map(lambda no: no*no, num))
print(op)

# task
prices=[100,200,300,400,500]

op= list(map(lambda no: (no*10)/100))
print(op)