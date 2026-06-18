class demo:
     
    #class variable 
    name="Payal"

    #instance variable
    #def __init__(self):
     #   self.name1("Payal")

    @staticmethod
    def welcome():
        print("hello its static method")

        #class variable is accessed by static methods by using classname itself 
        print("Class variable value is:",demo.name)

        #instance variable can't be accessed by static methods
        #print("instance variable value is:",demo.name1)


demo.welcome()
    
        



