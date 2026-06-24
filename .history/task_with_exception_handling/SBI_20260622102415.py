from bank import bank

class SBI(bank):

    def deposit(self, amount):
        total=0
        total= self.__bal+ amount
        self.setBal(total)
        print()