class demo:
    #class variable
    ins_name="Payal"

#class method
@classmethod
def update(cls):
    new_value=input("Enter new name:")
    cls.ins_name= new_value
    print("Updated")

#1. 1st way to call class variable
demo.update()
print(f"updated name is {demo.ins_name}")

#2. 2nd way to call class variable
obj= demo()
obj.update()
print("updated name is:", demo.ins_name)
