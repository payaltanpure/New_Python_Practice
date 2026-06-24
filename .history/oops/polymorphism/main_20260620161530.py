#this file is used to run both child classes together and calling the parent class abstarct methods in a single file using child class objects , 
#done same like hierarchical inheritance becoz the here the structure is same like hierarchical inheritance here also
from gpay import gpay
from phonepay import phonepay

print("Payment Options")

choice= input("Enter y/n")

if choice=='y':
    print("1.Gpay\n2.PhonePay")
    ip= int(input("Enter your choice:"))

    while True:
        if ip==1:
            #object of gpay class
            payment= gpay()
            break;
        elif ip==2:
            #object of phonepay class
            payment=phonepay()
            break;
        else:
            break;

else:
    print("Ok No problem ")


#called the parent class abstract methods using 
payment.pay()