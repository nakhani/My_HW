import random
import arcade
from apple import Apple
from snake import Snake
from frog import Frog
from shit import Shit

class Game(arcade.Window):
   
   def __init__(self):
       super().__init__(width=500,height=500,title="Super Snake 🐍")
       self.background = arcade.load_texture("photos\—Pngtree—cartoon gray land plant free_4620256.png")
       self.text = arcade.load_texture("photos/a.png")
       self.food = []
       self.snake = Snake(self)
       self.run_update = True
       self.foodd()
       self.flag = 0


   def foodd(self):
       self.food.append(Apple(self))
       self.food.append(Frog(self))
       self.food.append(Shit(self))
        
      



   def on_draw(self):
       arcade.start_render()
       arcade.set_background_color(arcade.color.KHAKI)
       arcade.draw_texture_rectangle(250,300,500,1000,self.background)
       if self.flag == 1:
           arcade.draw_texture_rectangle(self.width//2,self.height//2,400,250,self.text)
           self.run_update = False


       elif self.flag == 0:
           self.snake.draw()
           for food in self.food:
             food.draw()

           score_text = f" Score : { self.snake.score }" 
           arcade.draw_text ( score_text , self.width - 130 , 12 , arcade.color.CG_RED , 12, font_name="Kenney Future" )


       arcade.finish_render()


   def on_update(self, delta_time: float):
        
    if self.run_update == True:

        self.snake.move()
        for food in self.food:
          if arcade.check_for_collision(self.snake, food):
             self.snake.eat(food)
             self.food = []
             self.foodd()

        if (self.snake.center_x < 0 or self.snake.center_x > 500 or 
            self.snake.center_y < 0 or self.snake.center_y > 500 or self.snake.score < 0):
                self.flag = 1

        
    

   def on_key_release(self, symbol: int, modifiers: int):
        if symbol== arcade.key.UP:
           self.snake.change_x = 0
           self.snake.change_y = 1
        if symbol== arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol== arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        if symbol== arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0




if __name__ == "__main__":
    game = Game()
    arcade.run()