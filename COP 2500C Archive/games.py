# Gradi Tshielekeja Mbuyi
# COP 2500C
# 9/12/2021
# Assignment #2 Problem B: Knightro's New Game

import random

num = random.randint(1,100)

guess = input("For the UCF Golden Sword, has Knightro picked an odd or even number? ")

evenOdd = num % 2

if(evenOdd == 0):
    if(guess == "even"):
        print("You guessed correct!  The Golden Key is yours!")
    elif(guess == "odd"):
        print("I am sorry Knightro will look for someone else.")
elif(evenOdd == 1):
    if(guess == "odd"):
        print("You guessed correct!  The Golden Key is yours!")
    elif(guess == "even"):
        print("I am sorry Knightro will look for someone else.")
