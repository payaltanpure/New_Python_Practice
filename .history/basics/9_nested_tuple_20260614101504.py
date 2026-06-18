# # nested tuple 

# t= (1,2,(3,4),(5,6),(7,(8,9)))
# print(t[0])
# print(t[2])
# print(t[3][1])
# print(t[4][1][1])

# # concat
# x=(1,2)
# y=(3,4)
# print(x+y)


# # empty tuple
# empty=()
# print(id(empty))

# name= input("Enter the name ")
# id= int(input("enter id"))
# user= (name, id)
# print(user)

# empty= (empty+user)
# # here again new empty named tuple is created original empty named tuple created upside is not modified becoz tuples are immutable 
# print(empty)


# library management system 
# id title authorname price


books=()
while True:
    print("LMS\n1.Add book\n2.Update Book\n3.Display Book\n4.Delete Book\n5.Exit")
    choice= int(input("Enter your choice"))


if choice ==1:
    id= int(input("Enter book id"))
    title= input("Enter book name")
    authorname= input("Enter author name")
    price= float(input("Enter book price"))
    newbook= (id, title, (authorname, price))
    books= books+ newbook
    print("Book added successfully")

elif choice ==2:
    print("Book updated successfully")

elif choice==3:

    print("Book displayed successfully")

elif choice==4:
    print("Book deleted successfully")

elif choice==5:
    print("Exit")




