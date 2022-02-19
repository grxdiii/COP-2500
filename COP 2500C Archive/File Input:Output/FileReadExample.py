# Gradi Mbuyi
# Input and Output Notes

# Reading the File

fileHandle = open("output.txt", "r")

text = fileHandle.read()

numbers = text.split("\n")

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

for index in range(len(numbers)):
    if (numbers[index] % 2 != 0):
        print(numbers[index], "is not even!")

print(numbers)
fileHandle.close()
