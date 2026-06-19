from bankaccount import bankaccount

class loan(bankaccount):

    def __init__(self):
        self.amount=0

    def loan(self, amount):
        print("Loan amount is:", {self.amount})