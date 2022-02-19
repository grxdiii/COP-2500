# Gradi Tshielekeja Mbuyi
# COP 2500C
# 10/07/2021
# Assignment #5: Problem A

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

import math

def determinant():
    d = (b*b) - (4*a*c)

    return d

# When b^2-4ac = 0 there is one real root
def oneRoot():
    d = (b*b) - (4*a*c)
    d = math.sqrt(d)
    
    numerator = -b + d
    denomerator = 2 * a

    quadForm = numerator / denomerator

    return quadForm

# When b^2-4ac > 0 there is two real roots
def twoRoot():
    d = (b*b) - (4*a*c)
    d = math.sqrt(d)
    
    numeratorOne = -b + d
    numeratorTwo = -b - d
    denomerator = 2 * a

    quadFormOne = numeratorOne / denomerator
    quadFormTwo = numeratorTwo / denomerator

    return quadFormOne, quadFormTwo

if(determinant() == 0): 
    print("The quadratic has one root:", oneRoot())
elif(determinant() > 0):
    quadFormOne, quadFormTwo = twoRoot()
    print("The quadratic has two root:", quadFormOne, "and", quadFormTwo)
else:
    print("Sorry, that quadratic has complex roots.")
