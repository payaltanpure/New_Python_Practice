from B import B
from C import C

class D(B,C):

    def __init__(self,name, salary, age ):
        print("D cons")
        B.__init__(self, name, salary)
        C.__init__(self, name, age )


d= D("Payal", 1000, 10)
print(D.mro())

# D cons
# B con
# 1000
# A con Payal
# C con
# 10
# A con Payal
# [<class '__main__.D'>, <class 'B.B'>, <class 'C.C'>, <class 'A.A'>, <class 'object'>]

# A con Payal this constructor of grand parent class is called twice this diamond problem 
# why this A's con is called twice becoz we called it from iths two child classes B and C also , so twice it is called and two times the value to name var is set which is not valid this is
#called as diamond problem 

# solution to this is **kwargs
#using this we call the cons of grand parent A only once and also the value to the var of grand parent A class is set once only 
#and we use super() call to call grand parent class 