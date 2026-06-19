from camera import camera
from musicplayer import mpp
class sp(camera,mpp  ):

    def __init__(self, mp, playlist ,sim ):

        #this super call is not allowed in multiple inheritance as it creates confusion in argument passing due to MRO ,so there are three solutions on it 
        #TypeError: camera.__init__() takes 2 positional arguments but 4 were given
        # super().__init__(self,mp, playlist)
        # self.sim=sim


        #1) 1st way pass all para to parent para cons by intializing them here again using self
        self.mp=mp
        self.playlist=playlist
        self.sim= sim
        #values are set to all para of parent class para cons along with child class para cons also


        #2) 2nd way is to pass one parent class para con para with suoer and other with normal self
        # super().__init__(mp)
        # self.playlist=playlist
        # self.sim=sim

       
        #3) 3rd way is to pass one para of parent class para cons by super and one by classname and self
        # super().__init__(mp)
        # mpp.__init__(self, playlist)
        # self.sim=sim
        

        #4) 4th way is to pass para to both parent class para con by classname and self 
        # camera.__init__(self,mp)
        # mpp.__init__(self, playlist)
        # self.sim=sim


    def display_sp(self):
        print(f"{self.sim} inserted! ready to call")

s= sp("400mp", 100, "VI")
s.display_cam()
s.display_mp()
s.display_sp()