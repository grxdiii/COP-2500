# Gradi Tshielekeja Mbuyi
# COP 2500C
# 9/07/2021
# Day 4 - Notes

# If else statements
grade = float(input("What grade do you have in this coourse?\n"))

if(grade >= 90):
    print("A")
elif(grade >= 80):
    print("B");
elif(grade >= 70):
    print("C")
else:
    print("F")

# While loop

print("Menu")
print("1. Play a game")
print("2. Find my grade")
print("3. Quit")

option = int(input("Input the number choice\n"))

while (option != 3):

    if(option == 1):
        num = 7;
        guess = int(input("Guess my lucky number\n"))
        if(num == guess):
            print("You got it right!")
        else:
            print("You lose.")
    elif (option == 2):
        grade == int(input("What is your grade\n")
       
    print("Menu")
    print("1. Play a game")
    print("2. Find my grade")
    print("3. Quit")

    option = int(input("Input the number choice\n"))

