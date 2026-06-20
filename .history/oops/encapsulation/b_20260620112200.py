from a import a
class b(a):
    pass

b= b()

#acess protected method normally
b._m()

print(b._name)
b._name="Kiran"
print(b._name)