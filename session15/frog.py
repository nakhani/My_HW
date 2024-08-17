import random
from animals import Animals


class Frog(Animals):
    def __init__(self,game):
        super().__init__("photos\ccc.png")
        self.width = 40
        self.height = 40
        self.center_x = random.randint(10,game.width-10)
        self.center_y = random.randint(10,game.height-10)
        self.change_x = 0
        self.change_y = 0
        self.score = 2