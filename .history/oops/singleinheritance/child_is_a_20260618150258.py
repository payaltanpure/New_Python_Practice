from parent_is_a import animal

class child(animal):
    def food(self):
        print("Dog is pedigree")

    def __init__(self):

        print("Child class default constructor")
        #used to call parent class default constructor
        super().__init__()


c1= child()

c1.sound()
c1.food()