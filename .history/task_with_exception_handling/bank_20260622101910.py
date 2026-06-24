#abstact class bank
from abc import ABC, abstractmethod
class bank(ABC):

    def __init__(self):
        self.__bal=0

    #getter
    def getBal(self):
        return self.__bal
    
    #update bal
    def update(self, amount):
        self.__bal= amount


    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    #no