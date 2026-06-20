from a import a
class b(a):
    pass

b= b()

#acess protected method normally
b._m()
#acess protected var normally
print(b._name)
b._name="Kiran"
print(b._name)