from bankaccount import bankaccount
from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):
    
    def __init__(self, name, bal):
        savingaccount.__init__(self, name, bal)
        loan.__init__(self, name, bal)


    def cus_info(self):
        print(f"Customer info is :")


c= customer("Payal", 10000)
c.cus_info()
c.show_acc()
c.deposit(1000)
c.loan(50000)