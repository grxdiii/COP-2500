# Gradi Tshielekeja Mbuyi
# COP 2500C
# 10/21/2021
# Notes

import pygame

pygame.init()

screen = pygame.display.set_mode( [500,500] )

circlePos = [250, 250]

running = True
while running == True:

    # Getting input of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circlePos[0] = circlePos[0] - 5

    # Actions
    circlePos[0] = circlePos[0] + 2

    if (circlePos[0] > 550):
        circlePos[0] = -25
    
    screen.fill( (255, 255, 255) )

    pygame.draw.circle(screen, (0,0,255), (circlePos[0], circlePost[1]), 75)

    pygame.display.flip()

pygame.quit()
