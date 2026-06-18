class demo:
    # class variable
    ins_name = "Payal"

    # class method
    @classmethod
    def update(cls, name):
        new_value = input("Enter new name: ")
        cls.ins_name = new_value
        print("Updated")



