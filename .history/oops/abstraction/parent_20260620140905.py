from abc import ABC, abstractmethod
#abstract class created using above statement=> from abc import ABC, abstractmethod
class parent(ABC):

    #abstarct method declared
    @abstractmethod
    def start(self):
        #this is optional 
        print("Parent started, it is abstract method")


    def normal_method(self):
        print("Normal method")


# p= parent()
# p.start()