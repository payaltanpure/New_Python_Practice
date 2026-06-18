#imported parent class stud in college.py file that is child class
from stud import stud
class college:
    #class var
    uname="SPPU"

    #instance var with para con
    def __init__(self, cname, cloc):
        self.cname=cname
        self.cloc=cloc
        # object of parent class stud is created here , para are passed becoz stud class has para cons in it
        self.stud=stud(1,"ram")
    
    #instance method
    def display_college(self):
        print(f"{self.cname} college is present at {self.cloc} belongs to {self.uname}")


c= college("AISSMS", "RTO")
c.display_college()


c.stud.display_stud()
c.stud.greet()
stud.greet()