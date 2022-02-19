# Gradi Tshielekeja Mbuyi
# COP 2500C
# 8/26/2021
# Variables and Input (Notes)

idcardGrade = 12

print("Id Card:", idcardGrade)

GradiGPA = 3.65

print("GPA: ", GradiGPA)

# Target

# The amount of things we're buying
# Putting int inside a variable

pens = 10
paper = 100

# The price of thing we're buying (for each items)

pensPrice = .10
paperCost = .25

totalPensPrice = pens * pensPrice
totalPaperCost = paper * paperCost

print("Pens Price: $", totalPensPrice, sep="")
print("Paper Cost: $", totalPaperCost, sep="")

# The total price of things we're buying

totalPrice = totalPensPrice + totalPaperCost

print("Total Price: $", totalPrice, sep="")

# Input

headPhones = int(input("How many headphones would you like to buy?\n"))
headPhonesPrice = 95.5 * headPhones

print("Head Phone Price: $", headPhonesPrice, sep="")

# Turtle

import turtle


# house 1
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.circle(50, 180)

turtle.forward(100)
turtle.right(90)


turtle.penup()
turtle.right(90)
turtle.forward(110)
turtle.left(180)
turtle.pendown()

# house 2
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.circle(50, 180)

turtle.forward(100)
turtle.right(90)

