class login:

    def __init__(self):
        self.uname= "admin"
        self.__pin=1234

    def getuname(self):
        print(self.uname)

    def getpin(self):
        print(self.__pin)

    def setuname(self):
        self