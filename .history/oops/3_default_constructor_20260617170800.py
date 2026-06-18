class demo:
    #default constructor
    def __init__(self):
        print("default con called")

    
    def __init__(self, name, age):
        self.sname=name
        self.sage=age


# obj= demo()
obj2= demo("Payal", 21)
print(obj2.sname, obj2.sage)