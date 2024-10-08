import arcade
import pickle
from spaceship import Spaceship
from enemy import Enemy
import json


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=400,title="spaceship")
        arcade.set_background_color(arcade.color.BLACK_LEATHER_JACKET)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.enemy = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol==97: #left_side
            self.me.center_x = self.me.center_x - self.me.speed
        elif symbol==100: #right_side
            self.me.center_x = self.me.center_x + self.me.speed
    
    def on_update(self, delta_time: float):
       self.enemy.center_y -= self.enemy.speed

window = Game()
arcade.run()






