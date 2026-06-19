from camera import camera
from musicplayer import mp
class sp(camera,mp  ):

    def __init__(self, sim, mp, playlist  ):
        self.sim= sim

    def display_sp(self):
        print(f"{self.sim} inserted! ready to call")

s= sp("VI", "400mp", 100)
