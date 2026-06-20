from gpay import gpay
from phonepay import phonepay

print("Payment Options")

choice= input("Enter y/n")

if choice=='y':
    print("1.Gpay\n2.PhonePay")
    ip= int(input("Enter your choice:"))

    while True:
        if ip==1:
            payment= gpay()
        el if ip==2:
            payment=phonepay()