class demo:
    #class variable
    ins_name="Payal"

#class method
@classmethod
def update(cls):
    new_value= input("Enter new name:")
    cls.ins_name= new_value
    print("Updated")

#1. 1st way to call class variable
demo.update()
print("updated ")