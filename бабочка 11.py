import turtle

turtle.shape('turtle')
def o(n):
    for i in range(1,360,n):
        turtle.forward(1)
        turtle.left(n)
    turtle.left(180)
    for i in range(1,360,n):
        turtle.forward(1)
        turtle.left(n)

for h in (2,3,4,6,10):
    o(h)
                   
