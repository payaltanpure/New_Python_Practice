from employee import emp

class tester(emp):
    
    #instance variable with para cons
    def __init__(self, id, name, sal, tool):
       super().__init__(id, name, sal)
       self.tool=tool
   
    def testing(self):
      print(f"{self.name} is testing")

# t= tester(2, "Anu", 55000, )
# t.display()
# t.testing()