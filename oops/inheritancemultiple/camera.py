class camera:

    # parent1 class para cons
    def __init__(self, mp):
        self.mp=mp

    def display_cam(self):
        print(f"Camera with {self.mp}")