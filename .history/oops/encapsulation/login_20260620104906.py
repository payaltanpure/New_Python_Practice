class login:

    def __init__(self):
        self.uname= "admin"
        self.__pin=1234

    def getuname(self):
        print(self.uname)

    def getpin(self):
        print(self.__pin)

    def setuname(self, newuname):
        self.uname= newuname
        print("User name updated")
    
    def setpin(self, oldpin, newpin):
        if self.__pin==oldpin:
            