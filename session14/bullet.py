
import arcade
from enemy import Enemy

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__("photos\IMG_7820.PNG")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 3
        self.change_x = 0
        self.change_y = 1
        

    def move(self):
    
      self.center_y += self.speed

        