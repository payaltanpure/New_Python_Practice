class demo:
    # class variable
    ins_name = "Payal"

    # class method
    @classmethod
    def update(cls):
        new_value = input("Enter new name: ")
        cls.ins_name = new_value
        print("Updated")


# 1st way to call class method
demo.update()
print(f"Updated name is {demo.ins_name}")

# 2nd way to call class method
obj = demo()
obj.update()
print("Updated name is:", obj.ins_name)