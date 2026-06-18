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

#called using child class obj- parent class obj - parent class methods()
stud.display_stud()

#static method of parent class called 
c.stud.greet()

#staich method of parent class called directly by its object no need of child class obj
stud.greet()