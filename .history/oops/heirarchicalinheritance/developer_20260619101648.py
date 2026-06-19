from employee import emp
class dev(emp):

    def __init__(self,id,name,sal skill):
        super().__init__
        self.skill=skill

 
    def coding(self):
        print(f"{self.name} write code using python")
   

# d= dev(1, "Payal", 34000)
# d.display()
# d.coding()