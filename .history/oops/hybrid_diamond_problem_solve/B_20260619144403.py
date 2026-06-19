from A import A

class B(A):
    #here the name para of parent class A is not used 
    def __init__(self, salary, **kwargs):

        super().__init__(**kwargs)
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
        