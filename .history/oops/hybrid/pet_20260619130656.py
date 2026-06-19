from dog import dog
from cat import cat

class pet(dog, cat):
    def pet_info(self):
        print("Dog and cat are pets")

p = pet()
p.sound()
p.bark()
p.meow()
p.pet_info()