class demo:

    #instance variable

    def __init__(self):
        self.__pin=1234
        self.name="Payal"

    def getName(self):
        return self.name

obj= demo()
print(obj.__pin)
print(obj.name)