import turtle

turtle.shape('turtle')
def f(n):
    turtle.left(90+180/n)
    turtle.forward(9*n)
    for i in range(1,n):
        turtle.left(360/n)
        turtle.forward(9*n)
    turtle.penup()
    turtle.right(90-180/n)
    turtle.forward(4+2*n)
    turtle.pendown()

for h in range(3,10):
    f(h)


    
