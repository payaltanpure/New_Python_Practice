class demo2:
   
   def __init__(self):
        self.__pin= 1090

   def update(self):
       self.__pin=6789
       print(self.__pin)

obj= demo2()
print(obj.__pin)
# AttributeError: 'demo2' object has no attribute '__pin'
obj.update()

