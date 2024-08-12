import random
import arcade

class Box(arcade.Window):
    def __init__(self):
        super().__init__(width=460,height=420,title="box")
        arcade.set_background_color(arcade.color.WHITE)
        self.diamond_size = 20  
        self.diamond_spacing = 25 

    def on_draw(self):
        arcade.start_render()
        for row in range(10):  
            for col in range(10): 
                x = 110 + col * self.diamond_spacing
                y = 100 + row * self.diamond_spacing
                if (row + col) % 2 == 0 :
                 color = arcade.color.RED  
                else:
                 color = arcade.color.BLUE
                arcade.draw_polygon_filled([
                    (x, y + self.diamond_size / 2),
                    (x + self.diamond_size / 2, y),
                    (x, y - self.diamond_size / 2),
                    (x - self.diamond_size / 2, y)
                ], color)
    


window = Box()
arcade.run()


