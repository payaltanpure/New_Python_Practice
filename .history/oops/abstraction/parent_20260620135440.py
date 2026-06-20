from abc import ABC, abstractmethod
class parent(ABC):

    #abstarct method declared
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def noraml_method(self):
        print("Normal method")
