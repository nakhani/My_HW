import random
import arcade
from apple import Apple
from snake import Snake

class Game(arcade.Window):
   
   def __init__(self):
       super().__init__(width=500,height=500,title="super snake 🐍")
       self.background = arcade.load_texture("photos\—Pngtree—cartoon gray land plant free_4620256.png")
       self.food = Apple(self)
       self.snake = Snake(self) 
      



   def on_draw(self):
       arcade.start_render()
       arcade.set_background_color(arcade.color.KHAKI)
       arcade.draw_texture_rectangle(250,300,500,1000,self.background)
       self.snake.draw()
       self.food.draw()

       arcade.finish_render()


   def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)

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