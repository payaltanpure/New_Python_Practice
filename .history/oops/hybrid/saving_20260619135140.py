from bankaccount import bankaccount

class savingaccount(bankaccount):

    def __init__(self, name, bal):

        #hierarchical inheritance
        #call to parent class para cons
        super().__init__(name, bal)
        #instance variable
        self.amount=0
    

    def deposit(self,amount):
        self.balance+= amount
        print("New balace is:", self.balance})