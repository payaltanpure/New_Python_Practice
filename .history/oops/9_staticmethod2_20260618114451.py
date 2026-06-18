class demo:
     
    #class variable 
    name="Payal"

    #instance variable
    #def __init__(self):
     #   self.name1("Payal")

    @staticmethod
    def welcome():
        print("hello its static method")
        print("Class variable value is:",demo.name)

        #instance variable can
        #print("instance variable value is:",demo.name1)


demo.welcome()
    
        



