# Gradi Tshielekeja Mbuyi
# COP 2500C
# Sep 27 2021
# Assignment #4: Problem A: Video Games

import random

groups = 0
gamesPlayed = 0

while (gamesPlayed < 20):
    groups = groups + 1
    print("Groups Visited #", groups, sep="")

    people = random.randint(1,4)

    if(people < 4):
        gamesPlayed = gamesPlayed + 1
        print("Games Played", gamesPlayed)

        again = random.randint(1,2)

        while(again == 1):
            gamesPlayed = gamesPlayed + 1
            print("Games Played", gamesPlayed)
            again = random.randint(1,2)
