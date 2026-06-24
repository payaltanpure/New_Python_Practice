from bank import bank

class HDFC(bank):

    def deposit(self, amount):
        total=self.getBal()
        total+=amount
        self.setBal(total)
        print("Your credited amount is:", amount)
        print("HDFC",super().checkbal())



    def withdraw(self, amount):
        bal= self.getBal()
        if amount < bal:
            bal-=amount
            self.setBal(bal)  
            print("Amount deducted is:", amount)
            print("HDFC",super().checkbal())   
        else:
            print("Insufficient Balance to withdraw")    

s= SBI()
# s.setBal(500)
s.deposit(1000)
s.withdraw(500)
