from bankaccount import bankaccount
from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):
    
    def __init__(self, name, bal):


        #multiple inheritance
        #both parent classes(saving , laon) has para cons so confusion is para meter passing so one solution out of 
        #by calling using class name we resolve issue of multiple inheritance, that both parent classes( saving and laon needs name , bal )para so confusion can occur so passed it by child class para cons by not able to do with super becoz of MRO confusion so used classname to doso
        #and then name, bal para again passed from child classes (saving , loan ) to their parent class para cons that is bankaccount by using super().__init__(name, bal) from both child classes para cons it is possible becoz it is hierarrchical inheritance not multiple inheritance 
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