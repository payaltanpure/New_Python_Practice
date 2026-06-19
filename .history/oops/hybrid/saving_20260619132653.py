from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, name, bal):
        super().__init__(name, bal)
        self
    
    def deposit(self):
        self.balance+= self.amount