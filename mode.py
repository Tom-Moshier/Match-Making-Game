# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button
import sys
import buttonDetect as d
import twoPlayerGame
import onePlayerGame
import textInput as t

#Narrative: Starts One player mode or Two player mode, allows for name entry
#PreConditions: import pygame, Button, sys, buttonDetect, twoPlayerGame,
#onePlayerGame, textInput, and must have parameters theme and cardSet
#PostConditions: when mode is selected user is sent to correct game
def mode(theme,cardSet):
    display_width = 800
    display_height = 600

    color1 = (123,213,155)
    white = (255,255,255)
    black = (0,0,0)

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    gameDisplay.fill(color1)

    font1 = pygame.font.SysFont("century", 100)
    title = font1.render("MODE", True, black)
    gameDisplay.blit(title, (250,50))

    onePlayer = Button.Button(gameDisplay, color1, white, (50,200),(180,60),\
                            "1 Player", color1)
    onePlayerText = Button.Button(gameDisplay,color1,color1,\
                                  (550,200),(192,60),"Player 1", color1)
    name1 = Button.Button(gameDisplay, color1, color1, (350,200),(180,60),\
                            "Name 1:", color1)
    name1.drawButton()

    twoPlayer = Button.Button(gameDisplay, color1, white, (50, 300),(180, 60),\
                            "2 Player", color1)
    twoPlayerText = Button.Button(gameDisplay,color1,color1,\
                                  (550,300),(192,60),"Player 2", color1)
    name2 = Button.Button(gameDisplay, color1, color1, (350,300),(180,60),\
                            "Name 2:", color1)
    name2.drawButton()

    back = Button.Button(gameDisplay, color1, white, (500, 525), (255, 50),\
                         "Main Menu", color1)

    whiteOutline = pygame.image.load("Pictures/whiteOutline.png")
    blackOutline = pygame.image.load("Pictures/blackOutline.png")
    gameDisplay.blit(blackOutline, (546,295))
    gameDisplay.blit(blackOutline, (546,195))

    player1 = "Player 1"
    player2 = "Player 2"

    pygame.display.update()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        if d.buttonDetect(onePlayerText):
            gameDisplay.blit(whiteOutline, (546,195))
            onePlayerText = t.textInput(gameDisplay,onePlayerText)
            player1 = onePlayerText.getText()
            if player1 == "":
                player1 = "Player 1"
            gameDisplay.blit(blackOutline, (546,195))

        if d.buttonDetect(twoPlayerText):
            gameDisplay.blit(whiteOutline, (546,295))
            twoPlayerText = t.textInput(gameDisplay,twoPlayerText)
            player2 = twoPlayerText.getText()
            if player2 == "":
                player2 = "Player 2"
            gameDisplay.blit(blackOutline, (546,295))

        if d.buttonDetect(back):
            running = False

        elif d.buttonDetect(onePlayer):
            running = False
            onePlayerGame.game(player1,theme,cardSet)
            

        elif d.buttonDetect(twoPlayer):
            running = False
            twoPlayerGame.game(player1, player2,theme,cardSet)

        else:
            running = True
