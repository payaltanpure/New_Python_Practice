from device import device
class mobile(device):

    def __init__(self, brand, sim):

        # call is given to parent class para con that is device
        super().__init__(brand)
        self.sim=sim


    def call(self):
        print("Calling")