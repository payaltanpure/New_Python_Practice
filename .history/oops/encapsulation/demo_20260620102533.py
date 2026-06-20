class demo:

    #instance variable

    def __init__(self):
        #private variable => syntax- __varname
        self.__pin=1234
        self.name="Payal"

    def getName(self):
        return self.__pin
    


obj= demo()
#can't access the private var like this need to build one 
# print(obj.__pin)
print(obj.getName())
print(obj.name)