from abc import ABC, abstractmethod

#one form base form created here 

class payment(ABC):
    # created abstarct method, common method in all other forms created by bthis base form
    @abstractmethod
    def pay(self):
        pass
