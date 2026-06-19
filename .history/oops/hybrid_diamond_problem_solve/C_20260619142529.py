from A import A

class C(A):
    def __init__(self, name, age):
        print("C con")
        self.age= age
        A.__init__(self, name)