import random
import arcade

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 15
        self.height = 18
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x = 0
        self.change_y = 0
        self.speed = 2
        self.colors = [arcade.color.DARK_GREEN, arcade.color.MINT_GREEN]
        self.score = 0
        self.body = []


    def draw (self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,
                                        self.height,self.colors[1])

        for i,part in enumerate(self.body):
           arcade.draw_rectangle_filled(part['X'],part['Y'],self.width,
                                        self.height,self.colors[(i%2)])
          


    def move(self):
          self.body.append({'X':self.center_x, 'Y':self.center_y})
          if len(self.body)> self.score:
              self.body.pop(0)
          self.center_x += self.change_x * self.speed
          self.center_y += self.change_y * self.speed

    def eat(self,food):
        self.score += food.score
        del food
        
