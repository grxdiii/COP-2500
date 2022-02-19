# Gradi Tshielekeja Mbuyi
# COP 2500C
# 9/07/2021
# Assignment #2: Problem A - Movie Going

groupRate = 7.50
studentRate = 8.50
generalRate = 9.75

num = int(input("How many people are going?\n"))

if(num == 1):
    num =  num * studentRate 
    print("The group's price is $", "%.2f"%num, sep="")
elif(num > 1 and num < 20):
    num = num - 1
    num = num * generalRate + 8.50
    print("The group's price is $", "%.2f"%num, sep="")
else:
    num = num * groupRate
    print("The group's price is $", "%.2f"%num, sep="")
