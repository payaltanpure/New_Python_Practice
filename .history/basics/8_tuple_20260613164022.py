t= (100,20,30,40,50)
print(t)
print(t[1])
print(t[-1])

# t[2]=100;
# tuple immutable in nature so not allowed

t=(1, "Payal", 89)
print(t[0])
print(type(t))

#loop
for item in t:
    print (item)

#empty tuple

# t=()
# t.append(10)
# we cant do this becoz tuple is immutable in nature


# inbuilt functions
# min
# max
# sum
# len 
# sorted 

t1= (100,20,33,1111,55,33)
print(sorted(t1))

# inbuilt methods
# count
# index
# index(no to find index of it , index after that index we have to find the specified no)
print(t1.index(33,4)) 
# output: 5

# tuple function
x=[1,2,3]
print(x)
print(type(x))
y= tuple(x)
print(y)
print(type(y))

# membership 
print(2 in x)
print(5 in x)
print(5 not in x)

min=x[0]
for ch in x:
    if ch < min:
        min=ch
print(min)


key = int(input)