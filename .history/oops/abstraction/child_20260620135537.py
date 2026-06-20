from parent import parent
#abrstact class created using above statement
class child(parent):
    def start(self):
        print("Child started, it is abstract method")

c=child()
c.start()

c.normal_method()