from bank import bank

class SBI(bank):

    def deposit(self, amount):
        total=self.getBal()
        total+=amount
        self.setBal(total)
        print("sbi",super().checkbal())



    def withdraw(self, amount):
        bal= self.getBal()
        if amount < bal:
            bal-=amount
            self.setBal(bal)  
            print("Amount deducted is:", amount)
            print("sbi",super().checkbal())   
        else:
            print("Insufficient Balance to withdraw")    

s= SBI()
# s.setBal(500)
s.deposit(1000)
s.withdraw(500)
