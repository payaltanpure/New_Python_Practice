from parent_is_a import animal

class child(animal):
    def food(self):
        print("Dong is pedigree")

    def __init__(self):
        super().__init__()

c1= child()
c1.sound()
c1.food()