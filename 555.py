from random import randint
import turtle


turtle.shape('turtle')
vx=5
g=10
vy=80
x=0
y=0.01
dt=0.1
for k in range(1,6):
    while y>0:
        x = x + vx*dt
        y = y + vy*dt
        vy = vy - g*dt
        turtle.goto(x,y)
    y=0.01
    vy=80
