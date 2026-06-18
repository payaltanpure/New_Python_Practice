class college:
    #class var
    uname="SPPU"

    #instance var
    def __init__(self, cname, cloc):
        self.cname=cname
        self.cloc=cloc
    
    #instance method
    def display_college(self):
        print(f"{self.cname} college is present at {self.cloc}")