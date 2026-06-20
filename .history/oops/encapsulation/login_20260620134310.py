class login:


    def __init__(self):
        #public instance var
        self.uname= "admin"
        #private instance var
        self.__pin=1234

  
    def getuname(self):
        print(self.uname)

    #public getter method to get private var outside the class
    def getpin(self):
        #accessed the private var inside the class without getter and setter we done it normally
        print(self.__pin)


    def setnewuname(self, newuname):
        self.uname= newuname
        print("User name updated")
    
    # public setter method to set, update private var value
    def setnewpin(self, oldpin, newpin):

        #accessed the private var inside the class without getter and setter we done it normally
        if self.__pin==oldpin:
            self.__pin=newpin
            print("Pin updated")
        else:
            print("Pin mismatched")




obj= login()
obj.getuname()
#accessed private var pin using 
obj.getpin()
obj.setnewuname("admin@123")
obj.getuname()
obj.setnewpin(1234, 7890)
obj.getpin()