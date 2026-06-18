class demo:
    #class variable
    ins_name="Payal"

#class method
@classmethod
def update(cls):
    new_value= input("Enter new name:")
    cls.ins_name= 