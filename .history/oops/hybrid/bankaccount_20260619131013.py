class bankaccount:

    def __init__(self, name, balance):
        self.name=name
        self.balance= balance

    def show_acc(self):
        print("Account details are :")
        print(f"cust_name: {self.name}")