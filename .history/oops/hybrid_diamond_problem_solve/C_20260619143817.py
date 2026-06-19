from A import A

class C(A):
    def __init__(self, age):
        print("C con")
        self.age= age
        print(f"{self.age}")
        super().__init__(self, name)