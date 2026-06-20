from parent import parent
class child(parent):

    #overrided the abstract class 
    def start(self):
       print("Child started, it is abstract method")

c=child()
c.start()

c.normal_method()