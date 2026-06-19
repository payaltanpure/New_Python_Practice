from saving import savingaccount
from loan import loan

class customer(savingaccount, loan):

    def cus_info(self):
        print(f"Customer info is :")


b= ban
c=customer(10000)
c.cus_info()