#create file in specified folder and open in x mode, and if file exists with same name then handled the exception
try:
    file = open("exceptionandfilehandling/demo.txt", 'x')
    print(file)
except FileExistsError as e:
    print(e)

#write content into file
file = open("exceptionandfilehandling/demo.txt", 'w')
file.write("Hello how are u?")
print("Content added ")

#read the file content
file = open("exceptionandfilehandling/demo.txt", 'r')
print(file.read())