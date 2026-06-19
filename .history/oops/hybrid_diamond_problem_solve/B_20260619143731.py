from A import A

class B(A):
    def __init__(self, name, salar, **kwargsy):
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
        super().__init__(self, name)