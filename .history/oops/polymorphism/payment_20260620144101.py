from abc import ABC, abstractmethod

#one form 
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
