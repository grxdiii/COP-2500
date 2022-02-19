# Gradi Tshielekeja Mbuyi
# COP 2500C
# Final Assignment
# Nov 11, 2021

# This should take a while
import math

# Solves right triangle
def rightTriangle():

    firstAngle = 90.0
    
    print("\nPerfect, this should be easy...")

    print("\nGiven that we're working with a right triangle, one of the degrees should be 90°")

    error = True

    while(error == True):
        isSecondAngle = input("\nIs there a second angle present? ")
        isSecondAngle = isSecondAngle.lower()
        isSecondAngle = isSecondAngle.strip()
    
        if(isSecondAngle == "yes"):
            
            error = False
            
            secondAngle = float(input("\nWhat's the degree of the second angle? (Enter without degree symbol): "))
            thirdAngle = 180 - firstAngle - secondAngle

            print("\nAngle C: 90.0°")

            invalid = True

            if(invalid == True):
                angleName = input("\nis the second degree A or B? ")
                angleName = angleName.upper()
                angleName = angleName.strip()
        
                if(angleName == "A"):
                
                    invalid = False
                    print("\nAngle A: ", secondAngle, "°", sep="")
                    print("Angle B: ", thirdAngle, "°", sep="")
                
                elif(angleName == "B"):

                    invalid = False
                    print("\nAngle B: ", secondAngle, "°", sep="")
                    print("Angle A: ", thirdAngle, "°", sep="")
                
                else:
                    print("\nInvalid input...")
                    invalid = True

        # sides = int(input("\nHow many sides are presents? "))
        
        # if(sides == 2):
            # s1 = float(input("\nFirst Side (Enter a number) :"))
            # s2 = float(input("\nFirst Side (Enter a number) :"))
                          
        elif(isSecondAngle == "no"):

            error = False

            sides = int(input("\nHow many sides are presents? "))

            if(sides == 2):

                print("Angle C: 90°")

                s1 = float(input("Side A: "))
                s2 = float(input("Side B: "))
        else:
            print("\nPlease try again...")

# def solver(a, b, c, A, B, C):

# def AAS(a1, a2, s1):

# def ASA(a1, s1, a2):

# def SAS(s1, a1, s2):

# def SSA(s1, s2, a1):
    

# def SSS(s1, s2, s3):


name = input("Enter your name: ")
name = name.title()

print("\nWelcome ", name, "!\n", sep="")
print("I heard that you've been struggling in Trig; Don't worry, that's why I'm here!\n")
print("How it works: ")
print(" 1. Using the given information, the program will solve the triangle.")
print(" 2. The program only supports integers (We won't be using radians).")
print(" 3. User should not include \"°\" symbol when entering the given degree.")

end = False
counter = 0

while(end == False):

    isRightTriangle = input("\nWill you be solving a right triangle today? ")
        
    isRightTriangle = isRightTriangle.lower()
    isRightTriangle = isRightTriangle.strip()
    
    if(isRightTriangle == "yes"):
        end = True
        rightTriangle()
        
    elif(isRightTriangle == "no"):
        print("\nThe program works with these six options: ")
        print(" 1. AAA: Three Angles.")
        print(" 2. AAS: Two Angles and a Side not between.")
        print(" 3. ASA: Two Angles and a Side between.")
        print(" 4. SAS: Two Sides and an Angle between.")
        print(" 5. SSA: Two Sides and Angle not between.")
        print(" 6. SSS: Three Sides.\n")

        areSidePresent = int(input("How many sides are given? "))

        if(areSidePresent > 3):
            print("\n I'm afraid you may not be dealing with a tringle.")
            
        elif(areSidePresent == 0):

            print("\nThe triangle cannot be solved.\n")

            print("Reasons: ")
            print(" 1. The triangle cannot be solve without knowing any of the sides.")
            print(" 2. If more than one angles are presents, you're dealing with an AAA triangle.")
            print(" 3. We need to know at least one side to go further.")

            invalid = True

            while(invalid == True):
                retry = input("\nWould you like to retry? ")
                retry = retry.lower()
                retry = retry.strip()

                if(retry == "yes"):
                    end = False
                    invalid = False

                elif(retry == "no"):
                    end = True
                    invalid = False
                    print("\nThank you for using my app!")
                    print("\n© Gradi Tshielekeja Mbuyi")
                else:
                    print("\nInvalid input...")
                
            
        elif(areSidePresent == 3):
            a = int(input("\nSide a: "))
            b = int(input("Side b: "))
            c = int(input("Side c: "))

        if(areSidePresent != 0):
            
            areAnglePresent = int(input("\nHow many angless are present?"))

            if(areAnglePresent == 3):
                A = int(input("\nAngle A: "))
                B = int(input("Angle B: "))
                C = int(input("Angle C: "))
                    
            # elif(areSidePresent == 3 and areAnglePresent == 0):
                # SSS()
                

        
