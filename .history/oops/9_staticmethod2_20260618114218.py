class demo:


    @staticmethod
    def welcome():
        print("hello its static method")

    
        


#1 way calling
demo.welcome()

#2 way calling
d1= demo()
d1.welcome()


#1 way calling
demo.add(2,3)

#2 way calling
d1.add(3,4)
