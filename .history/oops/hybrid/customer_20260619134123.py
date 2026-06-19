from bankaccount import bankaccount
from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):
    
    def __init__(self, name, bal):

        #by calling using class name we resolve issue of multiple inheritance, that both parent classes( saving and laon needs name , bal )para 
        savingaccount.__init__(self, name, bal)
        loan.__init__(self, name, bal)


    def cus_info(self):
        print(f"Customer info is :")

        #grand parent class method called in child class method
        super().show_acc()


c= customer("Payal", 10000)
c.cus_info()

#issue of multiple inheritance that both classes laon and saving parent class of customer class needs amount from child class customer , so confusion of passing amount to whic class exactly so we passe the amount value in their classes respectice instnace methods deposit and laon instead of passing and taking in its para cons
c.deposit(1000)
c.loan(50000)