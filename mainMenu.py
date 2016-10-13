# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button
import sys
import options
import buttonDetect as d
import mode
import highscores

#Narrative: Main title screen where game is run
#PreConditions: import sys, options, buttonDetect, mode , highscores
#PostConditions: Play game, go to options menu, view highscores or quit
def menu():
    screen = "menu"
    theme = "Questions"
    cardSet = "Sports"
    while screen == "menu":
        title = pygame.image.load("Pictures/title.png")
        blue = (164,0,213)
        red = (164,0,213)
        white = (255,255,255)
        purple = (164, 0, 213)
        gameDisplay = pygame.display.set_mode((800,600))
        gameDisplay.fill(purple)
        pygame.display.set_caption("Match Maker")
        gameDisplay.blit(title,(245,5))
        running = True
        
        play = Button.Button(gameDisplay,blue,white,(220,100),(137,50),\
                             "PLAY",purple)
        optionsButton = Button.Button(gameDisplay,red,white,(220,225),(230,50),\
                                      "OPTIONS",purple)
        highscoreButton=Button.Button(gameDisplay,blue,white,(220,350),\
                                      (330,50), "HIGHSCORES",purple)
        quitGame = Button.Button(gameDisplay,blue,white,(220,475),(135,55),\
                                 "QUIT",purple)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if d.buttonDetect(quitGame):
                running = False
                pygame.quit()
                quit()

            elif d.buttonDetect(play):
                running = False
                mode.mode(theme,cardSet)

            elif d.buttonDetect(optionsButton):
                running = False
                optionsList = options.options(theme,cardSet)
                theme = optionsList[0]
                cardSet = optionsList[1]

            elif d.buttonDetect(highscoreButton):
                running = False
                highscores.highscores()

            else:
                running = True
