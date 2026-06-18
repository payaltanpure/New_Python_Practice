class demo:

    @staticmethod
    def welcome():
        print("hello its static method")

    @staticmethod
    def add(a, b):
        print("Addition is:", (a+b))
        
#1 way calling
demo.welcome()

#2 way calling
d1= demo()
d1.welcome()



demo.add(2,3)

d1.add(3,4)
