from payment import payment

#different form of base form in payment.py 
class phonepay(payment):

    #overrided the abstarct method of parent class
    def pay(self):
        print("Payment done by phonepay")