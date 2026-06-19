from A import A

class C(A):
    def __init__(self, age, **kwargs):
        super().__init__(self, name)
        print("C con")
        self.age= age
        print(f"{self.age}")
        