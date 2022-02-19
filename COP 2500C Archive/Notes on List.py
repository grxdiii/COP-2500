# Gradi Tshielekeja Mbuyi
# COP 2500C
# 10/14/2021
# List notes

# empty list
assignmentGrades = []

grade = 0

def calcAverage(gradeList):
    total = 0
    for index in range(len(gradeList)):
        # print(index, gradeList[index])
        total = total + gradeList[index]

    return total / len(gradeList)

def weightedGrade(gradeList):
    total = 0
    courses = 0

    for index in range(len(gradeList)):
        if(index % 2 == 1):
            total = total + gradeList[index] * 2
            courses = courses + 2
        else:
            total = total + gradeList[index]
            courses = courses + 1
            
    return total / courses



while(grade != -1):
    grade = int(input("What grade did you get? (type -1 to exist) "))

    if (grade >= 0):
        # adds grade at the end of the list
        assignmentGrades.append(grade)

    print(assignmentGrades)
    
    print(calcAverage(assignmentGrades))

print("Weighted", weightedGrade(assignmentGrades))

lowest = min(assignmentGrades)
        
assignmentGrades.remove(lowest)
print("Dropped Lowest", calcAverage(assignmentGrades))
print("Max Grade", max(assignmentGrades))


