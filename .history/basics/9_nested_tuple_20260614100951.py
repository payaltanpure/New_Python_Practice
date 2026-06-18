# nested tuple 

t= (1,2,(3,4),(5,6),(7,(8,9)))
print(t[0])
print(t[2])
print(t[3][1])
print(t[4][1][1])

# concat
x=(1,2)
y=(3,4)
print(x+y)


# empty tuple
empty=()
print(id(empty))

name= input("Enter the name ")
id= int(input("enter id"))
user= (name, id)
print(user)

empty= (empty+user)
# here again new empty named tuple is created original empty named tuple created upside is not modified becoz tuples are immutable 
print(empty)


# library management system 
# id title authorname price


books=()
choice= int(input("Enter your choice"))

print("")


if choice ==1:
    id= int(input("Enter book id"))
    title= input("Enter book name")
    authorname= input("Enter author name")
    price= float(input("Enter book price"))
    books= books+ newbook(id, title, (authorname, price))



