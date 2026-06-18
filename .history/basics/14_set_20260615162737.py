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

# 4.discard(ele): if ele present removed if not present no error 
a.discard(7)
a.discard(1)
print(a)

# 5.pop() : pops random ele 
a.pop()
print(a)

# 6.clear(): all set empty
a.clear()
print(a)

# operational methods

a={1,2,3}
b={3,4,5}

#1. set1.union(set2): union all ele from set a and set b and return one set igonre duplicates prints only once
print(a.union(b))
print(a|b)

#2. intersection: return common ele from both sets
print(a.intersection(b))
print(a&b)

#3.difference: returns set 1 unique data ignores set 2 adata and duplicates of set1 
print(a.difference(b))
print(a-b)

#4.symmetric diff : gives all ele from set 1 and set 2 except common data 
print(a.symmetric_difference(b))
print(a^b)

# checking methods 
a={1,2}
b={1,2,3}

#1.subset()
print(a.issubset(b))
print(b.issubset(a))

#2.superset()
print(a.issuperset(b))
print(b.issuperset(a))

#3.disjoint
x={1,2}
y={3,4}
z={1,2}
print(x.isdisjoint(y))
print(x.isdisjoint(z))


# inbuild funstions
len, min,max, sum, sorted

# example 

js= {"Ram", "Rahul", "Radha"}
ps= {"ram", }