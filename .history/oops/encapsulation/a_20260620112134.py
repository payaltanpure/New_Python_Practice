class a:

    def __init__(self):
        #protected var
        self._name="Payal"

    # protected method
    def _m(self):
        print("Hello m")



a= a()

#acess protected method normally
a._m()

print(a._name)
#update value of protected var
a._name="Anu"
print(a._name)
