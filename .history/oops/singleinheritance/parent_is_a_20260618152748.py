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

    #parent class instance method that print the value of its variable declared in para con , and that para con is called in child class con and over there child class only value to parent class para con is passed 
    def display(self):
        print(self.category)