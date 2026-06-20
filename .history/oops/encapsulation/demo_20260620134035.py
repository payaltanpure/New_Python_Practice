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
    

    #public getter method to access above private method outside the class
    def access_private_method(self):
        return self.__private_method()
    
    #public type setter method to modify the private variables outside the class
    def setPin(self, newpin):
        #accessed the private var inside the class without getter and setter we done it normally
        self.__pin= newpin

obj= demo()
#can't access the private var like this need to build one getter method of public type which will return the private var using self 
# print(obj.__pin)

#called getter method to accesss private variable outside the class but is same file it returns __pin value ,  so this method is called inside the print fucntion
print(obj.getPin())

#called getter method to access private method outside the class
print(obj.access_private_method())

#accessed public var normally
print(obj.name)

#call setter method to set the new pin by accessing old pin private var
obj.setPin(7890)

#again call getter method to check weather the new pin is setted or not
print(obj.getPin())


#how to access forcefully the private var outside the class in same file , inside class we use getter and setter to access
#objectname._classname__private_var_name
#but how and why
# python changes __var to _classname__var
# so internally : print(obj._classname__var)
# this is called name mangling.
print(obj._demo__pin)

#note: if we do not write any return satatement in private method it returns none  by default so, write atleast one return statement in private mthod to avoid none in output