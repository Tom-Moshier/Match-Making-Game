# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button
import sys
import buttonDetect as d

#Narrative: Creates an option menu to change theme of cards and match set
#PreConditions: import pygame, sys, Button, buttonDetect, needs theme and
#cardSet Parameters, image files must exist
#PostConditions: return theme and cardSet
def options(theme,cardSet):
    display_width = 800
    display_height = 600

    #colors in rgb
    grey = (153,153,255)
    red = (169,17,58)
    white = (255,255,255)
    purple = (164,0,213)
    black = (0,0,0)
    green = (29, 210, 35)

    #Size of Game's display aka resolution (width and height in a tuple)
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    #Background Color
    gameDisplay.fill(grey)
    title = pygame.image.load("Pictures/option.png")
    gameDisplay.blit(title, (245,0))


    font1 = pygame.font.SysFont("century",50)
    themes = font1.render("THEMES",True, black)
    gameDisplay.blit(themes,(50,150))

    #Buttons
    theme1 = Button.Button(gameDisplay, red, white, (50,225),(220,50),\
                           "Questions",green)

    theme2 = Button.Button(gameDisplay, red, white, (340,225),(125,50),\
                           "Glass",green)

    theme3 = Button.Button(gameDisplay, red, white, (555,225),(155,50),\
                           "Clouds",green)
    switchSet = font1.render("SWITCH SET", True, black)
    gameDisplay.blit(switchSet,(50,325))

    set1 = Button.Button(gameDisplay, red, white, (67,400),(145,50),\
                         "Sports",green)

    set2 = Button.Button(gameDisplay, red, white, (335,400),(105,50),\
                         "Cars",green)

    set3 = Button.Button(gameDisplay, red, white, (555,400),(180,50),\
                           "Animals",green)

    back = Button.Button(gameDisplay, grey, white, (259,545),(255,50),\
                         "Main Menu",purple)
    
    setList = [set1,set2,set3]
    wrench = pygame.image.load("Pictures/wrench.png")
    gameDisplay.blit(wrench, (565,10))

    if theme == "Questions":
        theme1.drawButtonCover()
        theme1.drawText()
    elif theme == "Glass":
        theme2.drawButtonCover()
        theme2.drawText()
    else:
        theme3.drawButtonCover()
        theme3.drawText()
    if cardSet == "Sports":
        set1.drawButtonCover()
        set1.drawText()
    elif cardSet == "Cars":
        set2.drawButtonCover()
        set2.drawText()
    else:
        set3.drawButtonCover()
        set3.drawText()

    #Button Selections when clicked 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if d.buttonDetect(back):
            running = False

        if not theme == "Questions":
            if d.buttonDetect(theme1):
                theme1.drawButtonCover()
                theme1.drawText()
                theme2.drawButton()
                theme3.drawButton()
                theme = "Questions"

        if not theme == "Glass":
            if d.buttonDetect(theme2):
                theme2.drawButtonCover()
                theme2.drawText()
                theme1.drawButton()
                theme3.drawButton()
                theme = "Glass"

        if not theme == "Clouds":
            if d.buttonDetect(theme3):
                theme = "Clouds"
                theme3.drawButtonCover()
                theme3.drawText()
                theme2.drawButton()
                theme1.drawButton()

        if not cardSet == "Sports":
            if d.buttonDetect(set1):
                for element in setList:
                    element.drawButton()
                set1.drawButtonCover()
                set1.drawText()
                cardSet = "Sports"

        if not cardSet == "Cars":
            if d.buttonDetect(set2):
                for element in setList:
                    element.drawButton()
                set2.drawButtonCover()
                set2.drawText()
                cardSet = "Cars"

        if not cardSet == "Animals":
            if d.buttonDetect(set3):
                for element in setList:
                    element.drawButton()
                set3.drawButtonCover()
                set3.drawText()
                cardSet = "Animals"
    #Returns the value of what options were choosen          
    return [theme,cardSet]
