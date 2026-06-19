from A import A

class B(A):
    def __init__(self, salary, **kwargs):
        super().__init__(name)
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
        