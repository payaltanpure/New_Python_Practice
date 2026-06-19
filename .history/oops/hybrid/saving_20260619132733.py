from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, name, bal):
        super().__init__(name, bal)
        self.amount=0
    
    def deposit(self,amount):
        self.balance+= amount
        print("New balace is:", {})