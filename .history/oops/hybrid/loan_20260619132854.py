from bankaccount import bankaccount

class loan(bankaccount):

    def __init__(self, name, bal):
        super().__init__(name, bal)
        
        #instance variable
        self.amount=0

    def loan(self, amount):
        self.amount=amount
        print("Loan amount is:", {self.amount})