class login:


    def __init__(self):
        #public instance var
        self.uname= "admin"
        #private instance var
        self.__pin=1234

    #public method to get public var
    def getuname(self):
        print(self.uname)

    def getpin(self):
        print(self.__pin)

    def setnewuname(self, newuname):
        self.uname= newuname
        print("User name updated")
    
    def setnewpin(self, oldpin, newpin):
        if self.__pin==oldpin:
            self.__pin=newpin
            print("Pin updated")
        else:
            print("Pin mismatched")

obj= login()
obj.getuname()
obj.getpin()
obj.setnewuname("admin@123")
obj.getuname()
obj.setnewpin(1234, 7890)
obj.getpin()