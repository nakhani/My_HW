import random
import arcade 


class Rocket(arcade.Sprite):
    def __init__(self,game):
     super().__init__("photo/breakout_sprites.png")
     self.width= 150
     self.height= 30 
     self.center_x= game//2
     self.center_y= 80
     self.change_x= 0
     self.change_y= 0
     self.speed= 3
     self.w =game
     self.score= 0



    def move(self):
       if self.change_x == -1:
         if self.center_x > self.height + 60:
             self.center_x -= self.speed
       elif self.change_x == 1:
          if self.center_x < self.w- self.height:
             self.center_x += self.speed


class Ball(arcade.Sprite):
   def __init__(self,game):
        super().__init__("photo\ll.png")
        self.center_x= game.width//2
        self.center_y= game.height//2
        self.change_x= random.choice([-1,1])
        self.change_y= -1
        self.speed= 2
        self.width= 50
        self.height= 50


   def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Logo(arcade.Sprite):
     def __init__(self,x,y):
        super().__init__("photo/lego.png")
        #self.shape1 = arcade.load_texture("photo/lego.png")
        #self.shape2 = arcade.load_texture("photo/2.png")
        #self.shape3 = arcade.load_texture("photo/3.png")
        #self.shape4 = arcade.load_texture("photo/4.png")
        #self.shape5 = arcade.load_texture("photo/5.png")
        #self.list_shapes = [self.shape1,self.shape2,self.shape3,self.shape4,self.shape5]
        self.center_x = x
        self.center_y = y
        self.width = 40
        self.height = 40

     #def draw (self):
         #for shape in self.list_shapes:
                 #arcade.draw_texture_rectangle(self.width,self.height,self.center_x,self.center_y,self.shape1)
                 
        
    


class Health(arcade.Sprite):
    def __init__ ( self , x ) :
        super().__init__ ( "photo\kjh.png" )
        self.width = 70
        self.height = 20
        self.center_x = x
        self.center_y = 15


class Game(arcade.Window):
   def __init__(self):
       super().__init__(width=550 , height=500, title= "BREAKOUT GAME")
       arcade.set_background_color(arcade.color.ARMY_GREEN)
       self.background = arcade.load_texture("photo/breakout_bg.png")
       self.text = arcade.load_texture("photo\—Pngtree—game over transparent background in_5995750.png")
       self.player = Rocket(self.height)
       self.ball = Ball(self)
       self.flag = 0
       self.x=20
       self.y=300
       self.blocks = []
       self.run_update = True
       self.heart_list = []
       self.shape_x = 42
       for i in range (3):
               new_heart= Health(self.shape_x)
               self.heart_list.append(new_heart)
               self.shape_x += 46

       for i in range(5):
            for _ in range(18):
                self.block = Logo(self.x, self.y)
                self.blocks.append(self.block)
                self.x += 30                
            self.y += 35
            self.x = 20

   def on_draw(self):
      arcade.start_render()
      arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)

      if self.flag == 1 :
          arcade.draw_texture_rectangle(self.width//2,self.height//2,400,250,self.text)
          self.run_update = False


      else:
       
       self.player.draw()
       self.ball.draw()

       for block in self.blocks:
                block.draw()
       for shape in self.heart_list:
               shape.draw() 


       score_text = f" Score : { self.player.score }" 
       arcade.draw_text ( score_text , self.width - 110 , 12 , arcade.color.LEMON_YELLOW , 12, font_name="Kenney Future" )

      arcade.finish_render()
      

   def on_update(self, delta_time: float):
    if self.run_update == True:
      
      self.player.move()
      self.ball.move()

 
      if self.ball.center_x < 30 or self.ball.center_x > self.width - 30 :
            self.ball.change_x *= -1 

      if self.ball.center_y > self.height -30:
          self.ball.change_y *= -1 

      if arcade.check_for_collision(self.player, self.ball):
          self.ball.change_y = 1 
      for count, block in enumerate(self.blocks):
        if arcade.check_for_collision(self.ball,block):
            self.ball.change_y = -1
            self.player.score += 1
            del self.blocks[count] 

      if self.ball.center_y <0:
             print ("LOSE!!!")
             if self.player.score ==0 or not self.heart_list:
                 self.flag = 1
             else:
               self.heart_list.pop(len(self.heart_list) - 1)
               self.player.score -= 1 
               del self.ball
               self.ball = Ball(self)


   def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
      
       if self.player.height + 60 < x < self.height- self.player.height:
        self.player.center_x = x


   def on_key_press(self, symbol: int, modifiers: int):

        if symbol== arcade.key.LEFT: 
            self.player.change_x = -1
        if symbol== arcade.key.RIGHT: 
            self.player.change_x = 1
        elif symbol == arcade.key.DOWN:
             self.player.change_x = 0
            

   def on_key_release(self, symbol: int, modifiers: int):
        self.player.change_x = 0





game = Game()
arcade.run()





