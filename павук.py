import turtle
n=int(input())
i=0
turtle.shape('turtle')
while i<n:
    i+=1
    turtle.forward(100)
    turtle.goto(0,0)
    turtle.left(360/n)
