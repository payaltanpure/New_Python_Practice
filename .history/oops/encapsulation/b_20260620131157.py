#access within child class 
from a import a
class b(a):
    pass

b= b()

#access within child class 
#acess protected method normally
b._m()
#acess protected var normally
print(b._name)

#update value of protected var
b._name="Kiran"
print(b._name)