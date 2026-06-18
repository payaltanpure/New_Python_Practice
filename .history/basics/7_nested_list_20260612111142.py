# x=[[1,2,3], [4,5,6],[7,8,9]]

# print(type(x))
# print(x[1])
# print(x[1][2])

# for i in x:
#     print(i)

# for row in x: #123
#     for col in row: #[123]
#         print(col, end=" ")

# #update
# x[1][1]=40
# print("\n",x)




student= [['Amit',20], ['Ram', 30], ['Sita', 89]]

# calling all values single single
# for row in student:
#         for col in row:
#             print(col)

# for row in student:
#         for col in row:
#             print(col[0], col[1])

#     print(col[0], col[1])
#           ~~~^^^
# TypeError: 'int' object is not subscriptable


# # calling same index value (ex: all name , marks, age, etc)
# for row in student:
#         print(row[0],":", row[1])

# # update 
# student[1][0]= "Payal"
# print(student)



# sum
sum=0
for marks in student: #['amit',10] , 2nd iteration: []
    sum+=marks[1] #10
print(sum)
