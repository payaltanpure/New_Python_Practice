from payment import payment

#one form of base form with diff behaviour , pay() method same as payment base form but behavior diff pay with gpay 
class gpay(payment):

    #overrided the abstarct method of parent class
    def pay(self):
        print("Payment done by gpay")