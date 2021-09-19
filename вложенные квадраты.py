import  turtle

turtle.shape('turtle')
for i in range(100,0,-10):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    
    
    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.pendown()

    turtle.forward(i-10)
    turtle.right(90)
    turtle.forward(i-10)
    turtle.right(90)
    turtle.forward(i-10)
    turtle.right(90)
    turtle.forward(i-10)
    turtle.left(180)
    
