import turtle

turtle.shape('turtle')
turtle.left(90)
def o(r,col):
    turtle.color(col)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

o(50,'yellow')
turtle.goto(-60,20)
o(7,'blue')
turtle.penup()
turtle.goto(-30,20)
turtle.pendown()
o(7,'blue')
turtle.penup()
turtle.goto(-69,-20)
turtle.pendown()
turtle.right(180)
turtle.color('red')
for i in range(1,180):
    turtle.forward(0.3)
    turtle.left(1)
turtle.penup()
turtle.goto(-50,-20)
turtle.pendown()
turtle.width(5)
turtle.color('black')
turtle.forward(20)
  
    
    
