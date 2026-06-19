from employee import emp
class dev(emp):

    def __init__(self, id, name, sal):
        super().__init__(id, name, sal)

    def coding(self):
        print(f"{self.name} write code using python")
   

# d= dev(1, "Payal", 34000)
# d.display()
# d.coding()