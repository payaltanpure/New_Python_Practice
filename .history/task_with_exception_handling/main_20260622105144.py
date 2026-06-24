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
    bank=HDFC()
else:
    print("Invalid chioce")
    exit()

while True:
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check Balance")

    ip=int(input("Enter your choice:"))
    if ip==1:
        amount=int(input("Enter amount to withdraw"))
        bank.withdraw(amount)
    elif ip==2:
        amount=int(input("Enter amount to deposit"))
        bank.deposit(amount)
    elif ip==3:
        bank.checkbal()
        