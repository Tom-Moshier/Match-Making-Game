# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button
import sys
import buttonDetect as d
import pickle

# Narrative: Gets the list of highscores
# Precondition: Must be called
# Postcondition: Returned a list of the top 10 high scores, inserting none and
# 0 for anywhere there was an empty slot
def getListOfScores():
    try:
        highscore = pickle.load(open("highscoresList.dat",'rb'))
        highscoresKeys = highscore.keys()
        highscoresList = list(highscoresKeys)
        for num in range(len(highscoresList)):
            highscoresList[num] = int(highscoresList[num])
        highscoresList.sort()
        listOfScores = []
        for value in range(10):
            try:
                listOfScores.append([highscoresList[value],\
                                     highscore[str(highscoresList[value])]])
            except:
                listOfScores.append([0,"None"])
    except:
        listOfScores = []
        for value in range(10):
            listOfScores.append([0,"None"])
    return listOfScores

# Narrative: Displays a page showing the top 10 high scores by time
# Precondition: Must be called
# Postcondition: Drew a page showing the top 10 high scores
def highscores():
    listOfScores = getListOfScores()
    display_width = 800
    display_height = 600

    color3 =  (204, 204, 0)
    white = (255,255,255)
    black = (0,0,0)


    gameDisplay = pygame.display.set_mode((display_width, display_height))
    gameDisplay.fill(color3)

    font1 = pygame.font.SysFont("century", 50)
    title = font1.render("HighScores", True, black)
    gameDisplay.blit(title, (250,10))

    line = pygame.image.load("Pictures/line.png")
    gameDisplay.blit(line, (398,75))

    font2 = pygame.font.SysFont("century", 30)
    onePlayer = font2.render("One Player", True, black)
    gameDisplay.blit(onePlayer, (130, 80))


    font3 = pygame.font.SysFont("century", 25)
    name = font3.render("Name", True, black)
    gameDisplay.blit(name, (60, 120 ))
    gameDisplay.blit(name, (460, 120 ))
    score = font3.render("Time", True, black)
    gameDisplay.blit(score, (280, 120))
    gameDisplay.blit(score, (680, 120))
    yCord = 180
    for number in range(5):
        nameAndScore = font3.render(listOfScores[number][1].title(),\
                                    True,black)
        gameDisplay.blit(nameAndScore,(60,yCord))
        nameAndScore = font3.render(format(listOfScores[number][0]/100000,\
                                           '.3f'),True,black)
        gameDisplay.blit(nameAndScore,(280,yCord))
        nameAndScore = font3.render(listOfScores[number+5][1].title(),True,\
                                    black)
        gameDisplay.blit(nameAndScore,(460,yCord))
        nameAndScore = font3.render(format(listOfScores[number+5][0]/100000,\
                                           '.3f'),True,black)
        gameDisplay.blit(nameAndScore,(680,yCord))
        yCord += 60

    trophy = pygame.image.load("Pictures/trophy.png")
    gameDisplay.blit(trophy, (200,30))
    gameDisplay.blit(trophy, (535,30))

    back = Button.Button(gameDisplay, color3, white, (260,540),(255,50),\
                         "Main Menu",color3)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if d.buttonDetect(back):
            running = False

        else:
            running = True
