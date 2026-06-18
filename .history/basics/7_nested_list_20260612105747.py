x=[[1,2,3], [4,5,6],[7,8,9]]

print(type(x))
print(x[1])
print(x[1][2])

for i in x:
    print(i)

for row in x: #123
    for col in row: #[123]
        print(col, end=" ")

#update
x[1][1]=40
print("\n",x)

# calling same index value (ex: all name , marks, age, etc)
student= [['Amit',20], ['Ran', ]
