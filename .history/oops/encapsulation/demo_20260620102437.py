class demo:

    #instance variable

    def __init__(self):
        
        self.__pin=1234
        self.name="Payal"

    def getName(self):
        return self.__pin
    


obj= demo()
print(obj.getName())
print(obj.name)