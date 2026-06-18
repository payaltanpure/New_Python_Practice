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
# 1.add: used to add one ele at a time
a={1,2}
a.add(3)
print(a)

# 2.update: used to add many elements in one time
# using update we cant update existiong ele because there is not indexing followed no array structure
a.update([4,5,6])
print(a)


# 3.remove
a.remove(4)
print(a)
# a.remove(7) error becoz 7 not present in set

# 4.discard(ele): if ele 