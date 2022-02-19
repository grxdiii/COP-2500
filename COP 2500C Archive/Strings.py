# Gradi Tshielekeja Mbuyi
# COP 2500C
# Strings
# 11/08/2021

# list of classes
courses = []

# condition for if statements and while loops
greaterThanFive = False
isDone = False

# inputs and outputs name of courses
def naming():

    # ask users to add classes to courses
    if(isDone == False and greaterThanFive == False):
        name = input("\nWhat courses would you like to take? ")
        name = name.title()
        items = name.split(",")

    # ask users to remove classes from courses
    elif(isDone == False and greaterThanFive == True):
        name = input("\nWhat courses would you like to drop? ")
        name = name.title()
        items = name.split(",")

    # adds classes to courses
    if(isDone == False and greaterThanFive == False):
        for item in items:
            courses.append(item.strip())
            
    # removes classes from courses
    elif(isDone == False and greaterThanFive):
        for item in items:
            courses.remove(item.strip())

    # prints out the courses list
    print("You are currently taking these courses:")
    for x in range(1, len(courses)+1):
        print(" ", x, ": ", courses[x-1], sep="")
    
# the actual program
print("You aren't currently taking any course. ")

# this condition will be met everytime the user starts/runs the program
while(isDone == False and greaterThanFive == False):

    # ask user to add courses
    # prints out the courses
    naming()

    # this condition will be met when user inputs more than 5 courses
    if(len(courses) > 5):
        greaterThanFive = True

        # the while loop will run until the items in courses are less than or equal to 5
        while(greaterThanFive == True and isDone == False):

            # ask user to remove courses
            # prints out the courses
            naming()

            # tells the program that courses has less than 5 items
            if(len(courses) < 5):
                greaterThanFive = False

            # tells the program that course has exactly 5 items
            # program ends
            elif(len(courses) == 5):
                isDone = True
                greaterThanFive = False

    # this condition will be met when user inputs exactly 5 courses
    # program ends
    elif(len(courses) == 5):
        isDone = True

print("\nDone!")
