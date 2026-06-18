from parent_is_a import animal

class child(animal):

    #instance method
    def food(self):
        print("Dog is pedigree")

    #default con
    def __init__(self):

        print("Child class default constructor")
        #used to call parent class default constructor
        super().__init__()

    #to call parent class method inside any child class method 
    def parent_class_method_access(self):
        super().sound()
        print("Parent class sound method called here")

#object of child class
#child classs default con called here 
c1= child()

#call to parent class method using child class object
c1.sound()

#call to child child method using child class object only 
c1.food()

c1.parent_class_method_access()

#same like java, c++