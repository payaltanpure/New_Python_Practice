from device import device
class mobile(device):

    def __init__(self, brand, sim):
        super().__init__(brand)
        self.sim=sim


    def call(self):
        print("Calling")