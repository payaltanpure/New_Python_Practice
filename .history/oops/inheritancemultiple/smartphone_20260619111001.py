from camera import camera
from musicplayer import mp
class sp(camera,mp  ):

    def __init__(self, sim, mp, playlist  ):
        # self.mp=mp
        # self.playlist=playlist
        # self.sim= sim

        # super().__init__(mp)
        # self.playlist=playlist
        # self.sim=sim

        super().__init__(mp)
        mp.playlist=playlist
        self.sim=sim


    def display_sp(self):
        print(f"{self.sim} inserted! ready to call")

s= sp("VI", "400mp", 100)
s.display_cam()
s.display_mp()
s.display_sp()