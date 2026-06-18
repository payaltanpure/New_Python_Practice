class stud:
    #instance variable
    def __init__(self):
        self.name=None
        self.age=0
    
    def __init__(self, name):
        self.name= name
        print("Instance vaiable value is:")
        


#objcet 
s1=stud()
#value assign
s1.name="Payal"
s1.age=20
print(s1.name, s1.age)

#objcet
s2=stud()
#value assign
s2.name="Anu"
s2.age=16
print(s2.name, s2.age)

