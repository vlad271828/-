import turtle

turtle.shape('turtle')
def o(n):
    turtle.left(n)
    for i in range(1,120):
            turtle.forward(1)
            turtle.left(3)
    turtle.right(n)

for h in range(0,360,60):
    o(h)
    
