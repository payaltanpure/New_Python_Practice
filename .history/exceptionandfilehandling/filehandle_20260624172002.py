#craete file in specified folder and open in x mode
try:
    file = open("exceptionandfilehandling/demo.txt", 'x')
    print(file)
except FileExistsError as e:
    print(e)

