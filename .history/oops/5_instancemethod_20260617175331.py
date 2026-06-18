class demo:
    #instance variable
    def __init__(self, name):
        self.name= name

    # instance method
    def update_name(self, new_name):
        self.name=new_name
        print("New name is:",self.name)

#instnace variable pas
obj= demo("Payal")
print("Current name is:", obj.name)
obj.update_name("Anu")