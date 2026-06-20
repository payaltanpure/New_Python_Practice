from abc import ABC, abstractmethod


class payment(ABC):
    #one form base form created as 
    @abstractmethod
    def pay(self):
        pass
