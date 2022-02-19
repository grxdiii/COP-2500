# Gradi Tshielekeja Mbuyi
# COP 2500C
# 8/27/2021
# Assignment #1: Problem A: Reflection Pond Measurements

# Allows user to input the radius of the pond
pondRadius = int(input("Enter the radius of the pond.\n"))

# radius squared (part of the area formula)
pondRadiusSquared = pondRadius * pondRadius

# pi times radius squared
area = (pondRadiusSquared * 3.14) / 2

# Returns the area of the pond
print ("Area =", area)
