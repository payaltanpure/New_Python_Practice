from employee import emp
class dev(emp):

    def developer(self):
        print(f"{self.name} write code using python")
   

d= dev(1, "Payal", 34000)
d.display()
