from A import A

class B(A):
    #here the name para of parent class A is not decalred again to set the vlaue to it and to use in this class , it is set using **kwargs 
    #and salary the new independent para of this own B class is set to salary using key value pair set that is set in child class of B that is D becoz call to B child class of D is from D parent class D
    def __init__(self, salary, **kwargs):

        super().__init__(**kwargs)
        print("B con")
        self.salary=salary
        print(f"{self.salary}")
       # print(self.name) accessible name also
        