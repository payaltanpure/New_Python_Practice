from bankaccount import bankaccount

class laon(bankaccount):

    def __init__(self, name, balance, amount):
        super().__init__(name, balance)
        self.amount=amount

    def 