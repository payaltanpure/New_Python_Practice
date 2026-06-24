from SBI import SBI
from HDFC import HDFC

print("Bank Managemnet System")
print("Choose Bank:")
print("1.SBI")
print("2.HDFC")

ip= int(input("Enter your choice:"))

if ip==1:
    bank= SBI()
elif ip==2:
     banl=HDFC()

