from abc import ABC, abstractmethod

#one form base form created as 
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
