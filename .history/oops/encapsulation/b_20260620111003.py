from a import a
class b(a):
    pass

b=b()
b._m()
print(b.__name)

b._name= "Kiran"
print()
