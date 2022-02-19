# Gradi Tshielekeja Mbuyi
# COP 2500C
# 8/31/2021
# Day 3 - Control Statements

import random

isStudent = input("Are you a student? ")

if(isStudent == "Yes" or isStudent == "yes"):
    print("Free or Discount")
    chances = random.randint(0,100)
    if(chances < 50):
        print("You go FREE!")
    else:
        print("You need to pay a discounted ticket price")
else:
    print("You didn't say you were a student")


number = 12.573922

print("The value", "%.4f"%number)
