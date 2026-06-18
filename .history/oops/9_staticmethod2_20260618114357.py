class demo:
     
    #class variable 
    name="Payal"

    #instance variable
    def __init__(self):
        self.name("Payal")

    @staticmethod
    def welcome():
        print("hello its static method")
        print("Class variable value is:",demo.name)
        print("instance variable value is:",)


demo.welcome()
    
        



