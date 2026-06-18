from stud import stud
class college:
    #class var
    uname="SPPU"

    #instance var with para con
    def __init__(self, cname, cloc):
        self.cname=cname
        self.cloc=cloc
        self.stud=stud()
    
    #instance method
    def display_college(self):
        print(f"{self.cname} college is present at {self.cloc} belongs to {self.uname}")


c= college("AISSMS", "RTO")
c.display_college()
c.stud.display_stud()
