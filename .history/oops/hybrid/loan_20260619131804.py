from bankaccount import bankaccount

class loan(bankaccount):

    def __init__(self):
        self.amount=0

    def loan(self):
        print("Loan amount is:", {self.amount})