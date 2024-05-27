
import turtle 


colors = ["red", "purple", "blue", "green", "yellow", "orange"]
P = turtle.Pen()
P.shape("turtle")
turtle.bgcolor('black')
P.penup()
P.pendown()
side=0
i = 0
c = 0
while i < 180 :
    for j in range(len(colors)):
        P.pencolor(colors[j])
        degree = ( ((i+3-2)*180) / (i+3) )
        P.left(180 - (degree / 2))
        side += 106

        while c <= i+2:
            P.forward( side / (i+3) )
            P.left(180 - degree)
            c += 1

        P.penup()
        P.right(180 - degree)
        P.right(degree / 2)
        P.forward(17)
        P.pendown()
        c=0
        i+=1
turtle.done()

