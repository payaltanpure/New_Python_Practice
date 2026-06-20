from abc import ABC, abstractmethod

#one form base form created here 

class payment(ABC):
    # created abstarct method, common method in all 
    @abstractmethod
    def pay(self):
        pass
