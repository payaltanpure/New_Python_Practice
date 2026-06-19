from A import A

class C(A):
    def __init__(self, name, age):
        print("C con")
        A.__init__(self, name)