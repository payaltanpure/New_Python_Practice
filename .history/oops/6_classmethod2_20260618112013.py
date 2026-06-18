class demo:
    # class variable
    ins_name = "Payal"

    # class method
    @classmethod
    def update(cls, name):
        cls.ins_name= name
        print("Updated name is:")



