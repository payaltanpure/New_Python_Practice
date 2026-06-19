from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, name, balance):
        super().__init__(name, balance)