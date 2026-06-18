class animal:

    #instance method
    def sound(self):
        print("Animal makes sound")

    #default con 
    def __init__(self):
        print("Parent class default constructor")
    
    #para con
    def __init__(self, cate):
        self.category= cate

    #parent class instance mthod the print the value of variable declared in para 
    def display(self):
        print(self.category)