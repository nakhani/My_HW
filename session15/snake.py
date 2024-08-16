import random
import arcade

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 25
        self.height = 25
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color = arcade.color.DARK_GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 2
        self.score = 0
        self.body = []


    def draw (self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        for part in self.body:
          arcade.draw_rectangle_filled(part['X'],part['Y'],self.width,self.height,self.color)


    def move(self):
          self.body.append({'X':self.center_x, 'Y':self.center_y})
          if len(self.body)> self.score:
              self.body.pop(0)
          self.center_x += self.change_x * self.speed
          self.center_y += self.change_y * self.speed

    def eat(self,food):
        self.score += 1
        del food
        
