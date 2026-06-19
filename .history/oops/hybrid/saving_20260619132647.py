from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, name, bal):
        super().__init__(name)
    
    def deposit(self):
        self.balance+= self.amount