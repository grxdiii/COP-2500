print("You aren't currently taking any course. ")
    
while(isDone == False and greaterThanFive == False):
    
    courseList = input("\nWhat courses would you like to take? ")
    courseList = courseList.title()
        
    subject = courseList.split(",")
    
    for item in subject:
        courses.append(item.strip())

    print("You are currently taking these courses:")

    for x in range(1, len(courses)+1):
        print(" ", x, ": ", courses[x-1], sep="")


    if(len(courses) > 5):
        greaterThanFive = True

        while(greaterThanFive == True and isDone == False):
            drop = input("\nWhat courses would you like to drop? ")
            drop = drop.title()
            
            dropping = drop.split(",")

            for item in dropping:
                courses.remove(item.strip())

            print("You are currently taking these courses:")

            for x in range(1, len(courses)+1):
                print(" ", x, ": ", courses[x-1], sep="")

            if(len(courses) < 5):
                greaterThanFive = False
            elif(len(courses) == 5):
                isDone = True
                greaterThanFive = False

    elif(len(courses) == 5):
        isDone = True

print("\nDone!")
