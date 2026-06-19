from B import B
from C import C

class D(B,C):

    def __init__(self,name):
        print("D cons")
        B.__init__(self)
        C.__init__(self)


d= D()
print(D.mro())

# D cons
# B con
# A con
# C con
# A con
# [<class '__main__.D'>, <class 'B.B'>, <class 'C.C'>, <class 'A.A'>, <class 'object'>]