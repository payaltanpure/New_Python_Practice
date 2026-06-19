from A import A

class B(A):
    def __init__(self, name, salary):
        print("B con")

        A.__init__(self, name)