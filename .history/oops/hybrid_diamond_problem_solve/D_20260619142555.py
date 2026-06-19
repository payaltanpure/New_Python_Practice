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
# A con
# C con
# A con
# [<class '__main__.D'>, <class 'B.B'>, <class 'C.C'>, <class 'A.A'>, <class 'object'>]