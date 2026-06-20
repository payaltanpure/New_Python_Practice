from payment import payment

class gpay(payment):

    #overrided the abstarct method of parent class
    def pay(self):
        print("Payment done by gpay")