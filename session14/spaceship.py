import arcade 
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self,w):
     super().__init__("photos/toppng.com-spaceship-png-358x576.png")
     self.center_x= w //2
     self.center_y=80
     self.change_x = 0
     self.change_y = 0
     self.width=48
     self.height=48
     self.speed = 2
     self.w = w
     self.bullets = []


    def move(self):
       if self.change_x == -1:
         if self.center_x > 0:
             self.center_x -= self.speed
       elif self.change_x == 1:
          if self.center_x < self.w:
             self.center_x += self.speed


    def fire(self):
       new_bullet = Bullet(self)
       self.bullets.append(new_bullet)