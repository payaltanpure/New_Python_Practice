from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):

    def cus_info(self):
        print(f"Customer info is :")


c= customer("Payal", 10000, )