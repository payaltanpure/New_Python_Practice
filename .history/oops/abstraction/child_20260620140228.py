from parent import parent
class child(parent):
    def start(self):
    pass
       print("Child started, it is abstract method")

c=child()
c.start()

c.normal_method()