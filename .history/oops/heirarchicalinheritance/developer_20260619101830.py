from employee import emp
class dev(emp):

    def __init__(self,id,name,sal, skill):
        #call given to parent class=> employee.py 
        super().__init__(id, name, sal)
        self.skill=skill

 
    def coding(self):
        print(f"{self.name} write code using {self.skill}")
   

# d= dev(1, "Payal", 34000, "Python")
# d.display()
# d.coding()