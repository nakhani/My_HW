import random 
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, game):
     super().__init__("spaceship\photos\—Pngtree—alien spaceships ufo with blue_6329025.png")
     self.center_x=random.randint(0,game.width)
     self.center_y=game.height + 24
     self.width=48
     self.height=48
     self.angle=180
     self.speed=2

    def move(self):
       self.center_y -= self.speed