from abc import ABC, abstractmethod


class payment(ABC):
    # created as abstarct method
    @abstractmethod
    def pay(self):
        pass
