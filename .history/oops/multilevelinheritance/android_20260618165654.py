from mobile import mobile
class android(mobile):

    def __init__(self, brand, sim, m):
        super().__init__(brand, sim)
    def take_photo(self):
        print("Smile Please")



oppo= android()
oppo.power()
oppo.call()
oppo.take_photo()