from A import A

class B(A):
    #here 
    def __init__(self, salary, **kwargs):

        super().__init__(**kwargs)
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
        