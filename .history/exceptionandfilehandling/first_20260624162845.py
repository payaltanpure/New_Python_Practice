# print("Start-->")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("dont divide by zero")
# print("End--->")


# try:
#   ip = int(input("Enter no"))
#   print(ip/2)
# except ValueError:
#   print("only nos allowed")

try: 
    ip1=int(input("Enter divisor"))
    ip2=int(input("Enter dividend"))
    print(ip2/ip1)
except ZeroDivisionError:
    print("dont didvide by 0")
except ValueError:
    print("only nos allowed")



