#abstact class bank
from abc import ABC, abstractmethod
class bank(ABC):

    def __init__(self):
        self.__bal=0

    #getter
    def getBal(self):
        return self.__bal
    
    #update bal, setter 
    def setBal(self, amount):
        self.__bal= amount


    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    #normal method 
    def checkbal(self):
        print("Your current available bal is:")
        #self.setBal()
        (self.__bal)

    