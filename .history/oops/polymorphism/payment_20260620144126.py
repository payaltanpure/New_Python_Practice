from abc import ABC, abstractmethod


class payment(ABC):
    #one form base form created as abstarct method
    @abstractmethod
    def pay(self):
        pass
