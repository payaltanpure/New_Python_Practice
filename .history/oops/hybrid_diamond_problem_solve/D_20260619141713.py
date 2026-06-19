from B import B
from C import C

class D(B,C):

    def __init__(self):
        print("D cons")
        B.__init__(self)
        C.__init__(self)


d= d()