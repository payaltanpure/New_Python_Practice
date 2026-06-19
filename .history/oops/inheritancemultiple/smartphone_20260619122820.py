from camera import camera
from musicplayer import mp
class sp(camera,mp  ):

    def __init__(self, mp, playlist ,sim ):

        super().__init__(mp, playlist)
        self.sim=sim

        # self.mp=mp
        # self.playlist=playlist
        # self.sim= sim

        # super().__init__(mp)
        # self.playlist=playlist
        # self.sim=sim

        # camera.__init__(self ,mp)
        # mp.__init__(self, playlist)
        # self.sim=sim


    def display_sp(self):
        print(f"{self.sim} inserted! ready to call")

s= sp("400mp", 100, "VI",)
s.display_cam()
s.display_mp()
s.display_sp()