class demo:

    #instance variable

    def __init__(self):
        #private variable => syntax- __varname
        self.__pin=1234
        #public var
        self.name="Payal"


    #getter method of public type to access privte var __pin
    def getName(self):
        return self.__pin
    
    #private method=> syntax- 
    


obj= demo()
#can't access the private var like this need to build one getter method of public type which will return the private var using self 
# print(obj.__pin)

#called getter method it returns __pin value here so this method is called inside the print fucntion
print(obj.getName())

#accessed public var normally
print(obj.name)