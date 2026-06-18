from mobile import mobile
class android(mobile):

    def __init__(self, brand, sim, camera):
        super().__init__(brand, sim)
        self.camera= camera


    def take_photo(self):
        print("Smile Please")

    def display_android(self):
        oppo.power()
        print(f"Sim {self.sim} inserted!")
        oppo.call()
        print(f"Android has {self.camera}")
        oppo.take_photo()



oppo= android("OPPO", "Jio", "48mp")


