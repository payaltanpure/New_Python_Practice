from bankaccount import bankaccount
from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):
    
    def __init__(self, name, bal):
        savingaccount.__init__(self, name, self.balance)
        loan.__init__(self, name, bal)


    def cus_info(self):
        print(f"Customer info is :")


c= customer("Payal", 10000)
