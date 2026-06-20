from abc import ABC, abstractmethod
#abstract class created using above statement=> from abc import ABC, abstractmethod
class parent(ABC):

    #abstarct method declared
    @abstractmethod
    def start(self):
        #this is optional write pass or else to create empty abstract method
        print("Parent started, it is abstract method")


    #normal method
    def normal_method(self):
        print("Normal method")



#cant call abstract withon abstract class
# p= parent()
# p.start()

p=parent()
p.normal_method()