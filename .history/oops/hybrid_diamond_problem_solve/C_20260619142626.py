from A import A

class C(A):
    def __init__(self, name, age):
        print("C con")
        self.age= age
        print(f"{self.salary}")
        A.__init__(self, name)