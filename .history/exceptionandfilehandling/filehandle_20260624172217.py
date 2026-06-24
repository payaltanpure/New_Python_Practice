#create file in specified folder and open in x mode
try:
    file = open("exceptionandfilehandling/demo.txt", 'x')
    print(file)
except FileExistsError as e:
    print(e)

#write content into file
file = open("exceptionandfilehandling/demo.txt", 'w')
file.write("Hello how are u?")
print("Content added ")

file = open("exceptionandfilehandling/demo.txt", 'r')
print(file.read())