# Gradi Tshielekeja Mbuyi
# COP 2500C
# 9/09/2021
# For Loops

value = int(input("How many speakers did we have?"))

for count in range(1, value):
    print("Who was speaker #", count)
    speaker = input()

    print("Great! I am glad ", speaker, "was able to come")
