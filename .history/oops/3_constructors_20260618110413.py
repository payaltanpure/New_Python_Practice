class demo:
    #default constructor
    def __init__(self):
        print("default con called")

    #parameterized con
    def __init__(self, name, age):
        self.sname=name
        self.sage=age
        print(self)


#default con calling
# obj= demo()

#para con calling 
obj2= demo("Payal", 21)
print(obj2.sname, obj2.sage)

#para con calling 
obj3= demo("Anu", 16)
print(obj3.sname, obj3.sage)

