from abc import ABC, abstractmethod

#one form base form
class payment(ABC):
    # created abstarct method
    @abstractmethod
    def pay(self):
        pass
