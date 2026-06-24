from bank import bank

class SBI(bank):

    def deposit(self, amount):
        total=self.getBal()
        total+=amount
        self.setBal(total)
        print(super().checkbal())



    def withdraw(self, amount):
        bal= self.getBal()
        if amount < bal:
            bal-=amount
            self.setBal(bal)  
            print("sbisuper().checkbal())         

s= SBI()
s.setBal(500)
s.deposit(1000)
