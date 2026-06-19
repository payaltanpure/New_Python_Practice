from A import A

class B(A):
    #here the name para of parent class A is not decalred again to set the vlaue to it and to use in this class , it is set using **kwargs
    def __init__(self, salary, **kwargs):

        super().__init__(**kwargs)
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
       # print(self.name) accessible name also
        