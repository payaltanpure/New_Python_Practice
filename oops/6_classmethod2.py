class demo:
    # class variable
    ins_name = "Payal"

    # class method
    @classmethod
    def update(cls, name): #here we used para con to assign new value to class variable
        cls.ins_name= name
        print("Updated name is:", cls.ins_name)



d1= demo()
d1.update("Anu")
print(d1.ins_name)
