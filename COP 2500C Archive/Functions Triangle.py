# Gradi Tshielekeja Mbuyi
# COP 2500C
# Functions - Turtle

import turtle
import random

def FtoC (Fa):
    C = 5 / 9 * (Fa - 32)

    return C

def drawTriangle(length):
    for a in range(3):
        turtle.forward(length)
        turtle.left(120)

for t in range(100):
    drawTriangle(t)
    turtle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.forward(200)
    turtle.setpos(x,y)
    turtle.pendown()
