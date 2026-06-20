from abc import ABC, abstractmethod
#abrstact class created using above statement
class parent(ABC):

    #abstarct method declared
    @abstractmethod
    def start(self):
        pass

    def normal_method(self):
        print("Normal method")
