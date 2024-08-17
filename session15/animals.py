import arcade

class Animals(arcade.Sprite):
    def __init__(self, animal):
        super().__init__(animal)
        self.width = 40
        self.height = 40
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0