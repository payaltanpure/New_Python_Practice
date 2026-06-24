
#1. ZeroDivisionError
# print("Start-->")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("dont divide by zero")
# print("End--->")


#2.ValueError
# try:
#   ip = int(input("Enter no"))
#   print(ip/2)
# except ValueError:
#   print("only nos allowed")


#3.Multiple exception handeld by multple except block as per your input the except block will get executed
# try: 
#     ip1=int(input("Enter divisor"))
#     ip2=int(input("Enter dividend"))
#     print(ip2/ip1)
# except ZeroDivisionError:
#     print("dont didvide by 0")
# except ValueError:
#     print("only nos allowed")

# 4. BaseException  it is used when we not many except blocks to handle many type of errors we use the base class that is BaseException which through message which we write to all types of Exception
# finally: runs always even idf excepton occur or not occur
# try:
#     print(10/0)
# except BaseException:
#     print("Somethings went wrong")
# finally:
#     print("I always execute")



#used to through inbuilt message of Base class rather than user defined error handling message 
try:
    print(10/0)
except BaseException as e:
    print(e)
finally:
    print("I always execute")


try:
    print(10/a)
except BaseException as e:
    print(e)
finally:
    print("I always execute")

# output:
# division by zero
# I always execute
# name 'a' is not defined
# I always execute


if (1234==1234):
    print("Password matched")
    