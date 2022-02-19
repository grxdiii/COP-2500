# Gradi Tshielekeja Mbuyi
# COP 2500C
# 8/31/2021
# Day 3 - Review, Math, Control Statements

money = int(input("How much money do you have? "))

# Integer Division - Always rounds down
# Number without the remainder
tickets = money // 10

# Modulus - Remainder
# Returns the numerator when there's an improper fraction

leftover = money % 10

print("The number of tickets you can buy are:", tickets)
print("You have $", leftover, " left over", sep="")

