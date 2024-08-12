import arcade
import random
from spaceship import Spaceship
from enemy import Enemy




class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=400,title="spaceship")
        self.background = arcade.load_texture("photos\image-from-rawpixel-id-12779138-png.png")
        self.GOVER_background = arcade.load_texture("photos\image-from-rawpixel-id-12779138-png.png")
        self.text = arcade.load_texture("photos\Lovepik_com-450063859-blue game over text style effect.png")
        self.me = Spaceship(self.width)
        self.enemies = []
        self.score = 0
        self.flag = 0
        

    def on_draw(self):
        arcade.start_render()
        if self.flag == 1:
           arcade.set_background_color(arcade.color.BLACK)
           arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.GOVER_background)
           arcade.draw_texture_rectangle(self.width//2,self.height//2,400,200,self.text)

        else:
           arcade.set_background_color(arcade.color.BLACK)
           arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        
           self.me.draw()

        

           for enemy in self.enemies:
               enemy.draw()

           for bullet in self.me.bullets:
               bullet.draw()
               
           score_text = f" Score : { self.score }" 
           arcade.draw_text ( score_text , self.width - 120 , 12 , arcade.color.CG_RED , 12, font_name="Kenney Future" )


    def on_key_press(self, symbol: int, modifiers: int):

        if symbol== arcade.key.LEFT: 
            self.me.change_x = -1
        if symbol== arcade.key.RIGHT: 
            self.me.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.me.change_x = 0
        elif symbol== arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0
    

    def on_update(self, delta_time:float):

        self.me.move()

        for bullet in self.me.bullets:
            bullet.move()

        if random.randint(1,130) == 6:
           self.new_enemy = Enemy(self)
           self.enemies.append(self.new_enemy)

        for enemy in self.enemies:
           enemy.move()
           if enemy.center_y < 0 :
               self.enemies.remove(enemy)
           
        for enemy in self.enemies:
            if arcade.check_for_collision(self.me, enemy):
               self.flag = 1

        for enemy in self.enemies:
            for bullet in self.me.bullets:
                if arcade.check_for_collision(enemy,bullet):
                    self.enemies.remove(enemy)
                    self.me.bullets.remove(bullet)
                    self.score += 1 



window = Game()
arcade.run()





