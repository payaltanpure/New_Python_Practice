from parent import parent
class child(parent):

    #overrided the abstract class of parent class
    def start(self):
       print("Child started, it is abstract method")

c=child()
c.start()

#called normal method of parent class
c.normal_method()