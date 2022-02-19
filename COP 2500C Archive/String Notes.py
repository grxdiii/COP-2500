# Gradi Mbuyi
# String Notes

choice = input("What would you like to do? ")

# splits based on spaces
words = choice.split()
print(words)

for word in words:
    if(word.lower() == "today"):
        print("I found today")

# Check to see if it is a title
# choice.title makes the text a title
print("Is title", choice.istitle())

#checks to see if it is a digit
print("Digit:", choice.isdigit())

#checks to see if it is lower case
print("Is lower:", choice.islower())

# find the index of a string
print(choice.find("Den"))

# Capitalize first letter (first word)
capital = choice.capitalize()
print("Capitalization:", capital)

# choice.upper() makes choices upper case

upper = choice.upper()
print("Upper:", upper)

lower = choice.lower()
print("Lower:", lower)

print("Original:", choice)





    
