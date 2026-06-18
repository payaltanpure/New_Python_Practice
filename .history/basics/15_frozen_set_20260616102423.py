x= frozenset([1,2,3,4,5])
print(x)
print(type(x))

a=frozenset([1,2,3])
b= frozenset([3,4,5])
print(a|b)
print(a&b)
print

#nested set 
# a={1,2,3,4}
# b={a}
# ps= {11,22,33,{33,44,55}}
# print(ps)
#not allowed nested set

# not allowed mixed data structure set
# ps= {11,22,33,[44,55,66]}
# print(ps)

# frozenset allows nested sets but not in traditional way 
# this is not allowed
# ps= frozenset([11,22,33],[44,55,66])
# print(ps)
fs= frozenset([11,22,33])
s={fs}
print(s)






