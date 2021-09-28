import math
from random import randint
import turtle

v=1
pool = [turtle.Turtle(shape='turtle') for i in range(10)]
for unit in pool:
unit.penup()
unit.speed(50)
unit.goto(randint(-30, 30), randint(-30, 30))


for k in pool:
k.left(randint(0,360))
X=[]
Y=[]
R=[]
for k in pool:
X.append(k.xcor())
Y.append(k.ycor())
R.append(k.heading())

for k in range(1,100):
for i in range(0,10):
X[i]+=v*math.cos(R[i]/57)
Y[i]+=v*math.sin(R[i]/57)
a=0
for s in pool:
s.goto(X[a],Y[a])
if Y[a]>40:
R[a]=-R[a]
s.left(2*R[a])
if Y[a]<-40:
R[a]=-R[a]
s.left(2*R[a])
a+=1
