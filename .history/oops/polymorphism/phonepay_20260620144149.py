from payment import payment

class phonepay(payment):

    #overrided the abstarct method of parent class
    def pay(self):
        print("Payment done by phonepay")