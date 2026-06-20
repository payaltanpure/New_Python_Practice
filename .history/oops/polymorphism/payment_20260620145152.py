#runtime polymorphism => achieved by method overriding => same method name and same parameters but different class 
#here example of runtime poly with abstraction also


#comiple time poly=> 
from abc import ABC, abstractmethod

#one form base form created here 

class payment(ABC):
    # created abstarct method, common method in all other forms created by bthis base form
    @abstractmethod
    def pay(self):
        pass


#pay() method is common in all payment options so it is declaed as abstract that is to be used in child classes again by overriding them, with diff behaviour 