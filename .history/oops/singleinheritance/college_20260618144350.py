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
#child class method is called by child object only , not by parent class 
c.display_college()


#parent class method called in child class using child class obj- parent class obj - parent class methods()
c.stud.display_stud()

stud.display_stud()

#static method of parent class called 
c.stud.greet()

#static method of parent class called directly by its object no need of child class obj
stud.greet()

