from bankaccount import bankaccount
from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):
    
    def __init__(self, name, bal):
        savingaccount.__init__(self, name, self.balance)
        loan.__init__(self)


    def cus_info(self):
        print(f"Customer info is :")


b= bankaccount("Payal", 10000)
c=customer(1000)
c.cus_info()
c.