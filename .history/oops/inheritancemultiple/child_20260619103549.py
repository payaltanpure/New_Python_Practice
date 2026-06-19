from parent1 import p1
from parent2 import p2

class c1(p1,p2):
    
    def xy(self):
        print("childxy method")

c= c1()
c.xyz()
c.abc()
c.xy()
c.common()
p2.common