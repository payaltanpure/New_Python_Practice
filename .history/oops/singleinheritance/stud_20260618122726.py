class stud():
   
   #instnace var with para con
   def __init__(self, sid, sname):
      
      self.sid= sid
      self.sname= sname
    
    #instance method
   def display_stud(self):
       print(f"student with id {self.sid} and name is {self.sname}")

    #static method
    @staticmethod
   

s= stud(1,"Payal")
s.display_stud()
   