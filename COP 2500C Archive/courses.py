# Gradi Tshielekeja Mbuyi
# COP 2500C
# 10/19/2021
# Assignment #6: Problem A: Course Selection

courses = []
subject = ""
drop = 0

while(subject != "EXIT"):
    subject = input("Which class would you like to take? (Enter EXIT once done) ")
    courses.append(subject)

    if(subject == "EXIT"):
        courses.remove("EXIT")
        print("Course Schedule: ", courses)
    elif(len(courses) < 6):
        print("Course Schedule:", courses)

    elif(len(courses) >= 6 and subject != "EXIT"):
        print("Course Schedule:", courses)

        while(drop < 1 or drop > 6):
            drop = int(input("You chose over 5 courses, which one would you like to drop? "))
 
        courses.pop(drop-1)

    drop = 0
        
