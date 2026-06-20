from abc import ABC, abstractmethod
#abstract class created using above statement=> from abc import ABC, abstractmethod
class parent(ABC):

    #abstarct method declared
    @abstractmethod
    def start(self):
        print("Parent started, it is abstract method")
        #pass

    def normal_method(self):
        print("Normal method")


# p= parent()
# p.start()