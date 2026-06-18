# x=[[1,2,3], [4,5,6],[7,8,9]]

# print(type(x))
# print(x[1])
# print(x[1][2])

# for i in x:
#     print(i)

# for row in x: #123
#     for col in row: #[123]
#         print(col, end=" ")

# printing in non lsit format
# for i in x:
#     print(i[0],i[1],i[2])



# #update
# x[1][1]=40
# print("\n",x)




student= [['Amit',20], ['Ram', 30], ['Sita', 89]]

# calling all values single single
# for row in student:
#         for col in row:
#             print(col)










# for row in student:
#     for col in student:
#         print(row[0], col[0])
# cant access like this with col reference so use row refernce only

# solution:
# # calling same index value (ex: all name , marks, age, etc)
# for row in student:
#         print(row[0],":", row[1])







# # update 
# student[1][0]= "Payal"
# print(student)



# sum
# sum=0
# for marks in student: #['amit',10] , 2nd iteration: ['payal',20]
#     sum+=marks[1] #10+20
# print(sum)


# find name whose marks greater than 80
# for marks in student:
#     if marks[1]>80:
#         print("name:", marks[0])


# append
student.append(["shiv", 99])
print(student)


student.append([ 99])
print(student)

student.append(["shiv"])
print(student)


print(student.index(["shiv", 99]))
# all methods and function of simple list applicable to nested list also

