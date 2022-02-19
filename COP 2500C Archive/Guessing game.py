import random

hiddenNumber = random.randint(1,100)

guess = -1

score = 0
maxGuesses = 6

play = True

wins = 0
loss = 0

while(play == True):

    while (guess != hiddenNumber and score < maxGuesses):

        guess = int(input("What is your guess? "))
        
        if(guess < hiddenNumber):
            print("You guessed to low.")
            score = score + 1
        elif(guess > hiddenNumber):
            print("You guess to high")
            score = score + 1
        else:
            print("You got it correct!")

    if(score == maxGuesses):
        print("You lose you guessed to many times")
        print("The correct answer was", hiddenNumber)
        loss = loss + 1
    else:
        print("Your score was", score)
        wins = wins + 1

    again = input("Would you like to play again?\n")
    if(again == "no"):
        play = False
    else:
        score = 0
        guess = -1
        hiddenNumber = random.randint(1,100)

print("You won", wins, "times and lost", loss, "times")
