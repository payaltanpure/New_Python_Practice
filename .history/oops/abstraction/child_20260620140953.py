from parent import parent
class child(parent):

    #overrided the 
    def start(self):
       print("Child started, it is abstract method")

c=child()
c.start()

c.normal_method()