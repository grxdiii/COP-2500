# Gradi Tshielekeja Mbuyi
# COP 2500C
# Sep 27 2021
# Assignment #4: Problem B: Icon Part 2

import turtle

turtle.pensize(10)
turtle.speed(10)

d = 0

# This loop puts the icon in 3 different columns
for i in range (3):
    # This loop puts the icon in 3 different rows 
    for i in range (3):
        # This loops is in charge of drawing the two circles
        for i in range(2):
            turtle.circle(100)
            turtle.penup()
            turtle.left(90)
            turtle.forward(10)
            turtle.right(90)
            turtle.pendown()
            turtle.color("gray")

        turtle.left(110)
        turtle.pensize(14)
        turtle.forward(100)
        turtle.left(95)
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(80)
        turtle.right(115)
        turtle.penup()
        turtle.forward(130)
        turtle.left(90)
        turtle.forward(225)

        turtle.pendown()
        turtle.color("black")

    turtle.penup()
    turtle.home()
    turtle.right(90)

    # I use the variable "d" to space out the icons by columnns
    d = d + 225
    turtle.forward(d)
    turtle.left(90)
    turtle.pendown()
    

    
