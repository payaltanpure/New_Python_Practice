from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, amount):
        self.amount= amount
    
    def deposit(self):
        self.balance+= self.amount