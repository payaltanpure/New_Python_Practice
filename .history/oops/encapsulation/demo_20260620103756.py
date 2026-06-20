class demo:

    #instance variable

    def __init__(self):
        #private variable => syntax- __varname
        self.__pin=1234
        #public var
        self.name="Payal"


    #getter method of public type to access privte var __pin
    def getPin(self):
        return self.__pin
    
    #private method=> syntax- def __methodname(self)
    def __private_method(self):
        #print("Hii")
        return("Its is private method")
    

    #public getter method to access above private method 
    def access_private_method(self):
        return self.__private_method()
    
    #public type setter method to modify the private variables
    def setPin(self, newpin):
        self.__pin= newpin

obj= demo()
#can't access the private var like this need to build one getter method of public type which will return the private var using self 
# print(obj.__pin)

#called getter method to accesss private variable it returns __pin value here so this method is called inside the print fucntion
print(obj.getPin())

#called getter method to access private method
print(obj.access_private_method())

#accessed public var normally
print(obj.name)

#call setter method to set the new pin by accessing old pin privte var

#note: if we do not write any return satatement in private method it returns none  by default so, write atleast one return statement in private mthod to avoid none in output