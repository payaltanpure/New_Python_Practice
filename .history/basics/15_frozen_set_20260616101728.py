x= frozenset([1,2,3,4,5])
print(x)
print(type(x))

a=frozenset([1,2,3])
b= frozenset([3,4,5])
print(a|b)
print(a&b)

#nested set 
a={1,2,3,4}
b={a}
#not allowed 

# frozenset allows nested sets
fs= frozenset([11,22,33])
s={fs}

