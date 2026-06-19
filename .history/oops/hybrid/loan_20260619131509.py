from bankaccount import bankaccount

class loan(bankaccount):

    def __init__(self, name, balance, amount):
        super().__init__(name, balance)
        self.amount=amount

    def loan(self):
        print("Loan amount is:", {self.amount})