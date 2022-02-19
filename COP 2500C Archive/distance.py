# Gradi Tshielekeja Mbuyi

import math

import turtle

import random

# Starter Code

def randomTurtle():

    for count in range(10):

        choice = random.randint(1,2)

    if (choice==1):

        turtle.forward(random.randint(5, 50))

    elif(choice==2):

        turtle.right(random.randint(1,359))

def testTurtle():

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)

# Call this when turning it in

randomTurtle()

# Call this when testing to make sure you have the correct answer

# testTurtle()

def distance(x, y):

    # stores the user's input
    
    x1 = x
    y1 = y

    # takes the position of the turtle
    
    x2 = turtle.xcor()
    y2 = turtle.ycor()

    # distance formula
    
    d = ((x2-x1)**2) + ((y2-y1)**2)
    d = math.sqrt(d)
    
    return d

print(distance(0, 0))
