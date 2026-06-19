from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, name, balance, amount):
        super().__init__(name, balance)
        self.amount= amount
    
    def deposit(self):
        self.balance+= self.amount