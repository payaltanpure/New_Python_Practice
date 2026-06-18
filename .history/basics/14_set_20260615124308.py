x={1,2,3,3,4,5}
print(x)
print(type(x))


y={}
print(type(y))

#2nd way - empty set created and then add ele in it by adding ele in list 
#becoz when we create empty set and check its type it is dict so add ele in it using list
y=set([1,2,3,4,4])
print(type(y))
print(y)

# methods
# 1.add
a={1,2}
a.add(3)
print(a)

# 2.update