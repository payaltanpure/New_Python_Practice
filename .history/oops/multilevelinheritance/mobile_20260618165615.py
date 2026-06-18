from device import device
class mobile(device):

    def __init__(self, brand, sim):
        super().__init__(brand)


    def call(self):
        print("Calling")