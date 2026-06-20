from payment import payment

#one form of base form with diff behaviour , pay() method 
class phonepay(payment):

    #overrided the abstarct method of parent class
    def pay(self):
        print("Payment done by phonepay")