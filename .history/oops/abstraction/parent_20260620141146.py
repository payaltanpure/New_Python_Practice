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



#can't call abstract method within abstract class, can't create object also of abstract class
# p= parent()
# p.start()
