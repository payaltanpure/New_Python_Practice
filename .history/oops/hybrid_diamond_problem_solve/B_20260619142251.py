from A import A

class B(A):
    def __init__(self, salry ):
        print("B con")

        A.__init__(self)