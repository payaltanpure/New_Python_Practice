from A import A

class B(A):
    def __init__(self, salary, **kwargs):
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
        