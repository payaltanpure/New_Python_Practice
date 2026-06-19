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


#parent common method la call using classname.methodname()
p1.common()
p2.common()

#both parent classes p1 & p2 has same method as common and child class also has that common method 
# then compiler gets confused whose common method should be called so that priority is set by MRO(Method resolving order)
#call depends on this sequence class c1(p1,p2)=> first child class c1's common method will be called then p1 parent's and then p2 parent's
# but now  when we call coomon method child class common method will be executed then how we will invoke parent class p1 p2's common method 
# so it is invoked by parent classname . common method name() eg. p1.common(), p2.common()
