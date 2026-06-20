from gpay import gpay
from phonepay import phonepay

print("Payment Options")

choice= input("Enter y/n")

if choice=='y':
    print("1.Gpay\n2.PhonePay")
    ip= int(input("Enter your choice:"))