from parent1 import p1
from parent2 import p2

class c1(p1,p2):
    
    def xy(self):
        print("childxy method")

    def common(self):
        print("child Common method")

c= c1()
c.xyz()
c.abc()
c.xy()
c.common()


#parent common method la call
p1.common()
