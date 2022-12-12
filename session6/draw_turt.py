import turtle 
import math

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
P = turtle.Pen()
P.shape("turtle")
P.right(30) 
turtle.bgcolor('black')
P.goto(0,0)
jump1 = 0
jump2 = 0
i=2
length = 30
while i < 180 :
    for j in range(len(colors)):
        P.pencolor(colors[j])
        length =+ 15
        i=i+1
        jump1 += 2
        jump2 += 5
        for c in range(i): 
            P.forward(length/ (2 * math.sin(math.pi / i)))     
            P.right(360/i)   
            
        P.up()
        P.goto(jump1,jump2)
        P.down() 
turtle.done()