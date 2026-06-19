class mpp:

    # parent2 class para cons     
    def __init__(self, playlist):
        self.playlist= playlist

    def display_mp(self):
        print(f"Music player has playlist of {self.playlist} songs")