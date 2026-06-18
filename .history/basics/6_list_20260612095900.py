# x= [10,20,30,40,77,99]

# sum=0
# even=0
# for ch in x:
#     sum+=ch
#     if ch%2==0:
#        even+=ch
# print("Sum of list ele is :", sum)
# print("Even ele sum is:", even)

x= [10,20,30,40,77,99]
max=0

for i in x:
    if x[i]>max:
        max= x[i]
print("Max element")