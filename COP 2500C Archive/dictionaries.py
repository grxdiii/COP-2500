# Gradi Tshielekeja Mbuyi
# COP 2500C
# Nov 18, 2021

# Dictionaries Notes

student = { "name" : "Gradi Mbuyi", "GPA" : 3.5 }

print(student)

# does the same thing
# get value 
print(student["name"])
print(student.get("name"))

print(student["GPA"])
print(student.get("GPA"))

# protects data from error
print(student.get("studentid"))

# second argument matters when student does not have "studentid"
# bruh moment is default value
print(student.get("studentid", "Bruh moment"))

# adding things to the dictionary
student["studentid"] = 1234567890
print(student.get("studentid", "Bruh moment"))

print(student)

# updates the dictionary
student.update( {"courses" : ["COP2500C", "ENC1101", "MAC2311"] } )

print(student)

student.update( {"studentid" : 987654321} )

print(student)
print(student["studentid"])

# remove things from dictionaries
student.pop("name")
print(student)

if "age" in student:
    student.pop("age")
    print("age removed")

print(student.pop("afda", "Not there"))
print(student)

# looping

# gets all keys
for key in student:
    print(key)
print(student.keys())

# gets all the values
for key in student:
    print(student[key])
print(student.values())

# print both key and value
for key, value in student.items():
    print(key, ":", value)

# clone
newStudent =  student.copy()
print(newStudent)
