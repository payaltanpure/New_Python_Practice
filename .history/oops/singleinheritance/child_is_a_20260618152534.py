from parent_is_a import animal

class child(animal):

    #instance method
    # def food(self):
    #     print("Dog is pedigree")

    # #default con
    # def __init__(self):

    #     print("Child class default constructor")

    #     #used to call parent class default constructor
    #     super().__init__() #parent class con called

    # #to call parent class method inside any child class method not in entire class we use below syntax
    # def parent_class_method_access(self):
    #     super().sound() #parent class method called here 
    #     print("Parent class sound method called here")

    #child class para con
    def __init__(self, cate):
        print("Child class Para con")
        #call given to parent class para con, and also passed the variable of parent class as a parameter to child class con, called as cate
        super().__init__(cate)
        
        



# #object of child class
# #child classs default con called here 
# c1= child()

# #call to parent class method using child class object
# c1.sound()

# #call to child child method using child class object only 
# c1.food()

# #call to child class method which accesses parent class method
# c1.parent_class_method_access()

#call to child class para con along with one para which is 
c2=child("Animal Category")
c2.display()


#same like java, c++