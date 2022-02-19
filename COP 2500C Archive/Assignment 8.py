# Gradi Tshielekeja Mbuyi

# courseList = "Sociology, english, CompSci   , psychology"

# print(courseList.strip() + "")
# print(courseList.split(","))


courseList = "a,b,c,d"

courses = courseList.split(",")
print(courses)

delete = "b"

if delete in courses:
    courses.remove(delete)

print(courses)


