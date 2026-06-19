from bankaccount import bankaccount

class loan(bankaccount):

    def __init__(self, name, bal):

        #hierarchical inheritance
        #call to parent class para cons
        super().__init__(name, bal)
        #instance variable
        self.amount=0


    def loan(self, amount):
        self.amount=amount
        print("Loan amount is:", self.amount})