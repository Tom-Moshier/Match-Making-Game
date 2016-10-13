# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button
import buttonDetect as d
import sys
import imageCheck
import random
import pickle
import getCards

#Narrative: Gets the messages into a list, returns them to game
#PreConditions: font1 and white must be passed into the function
#PostConditions: returns the list back to game
def getMessageList(font1,white):
    messageThree = font1.render("12 Points To Win",30,white)
    messageFour = font1.render("11 Points To Win",30,white)
    messageFive = font1.render("10 Points To Win",30,white)
    messageSix = font1.render("09 Points To Win",30,white)
    messageSeven = font1.render("08 Points To Win",30,white)
    messageEight = font1.render("07 Points To Win",30,white)
    messageNine = font1.render("06 Points To Win",30,white)
    messageTen = font1.render("05 Points To Win",30,white)
    messageEleven = font1.render("04 Points To Win",30,white)
    messageTwelve = font1.render("03 Points To Win",30,white)
    messageThirteen = font1.render("02 Points To Win",30,white)
    messageFourteen = font1.render("01 Point To Win",30,white)
    messageFifteen = font1.render("HighScore Saved!",\
                                  30,white)
    messageList = [messageThree,messageFour,messageFive,messageSix,\
                   messageSeven,messageEight,messageNine,messageTen,\
                   messageEleven,messageTwelve,messageThirteen,\
                   messageFourteen,messageFifteen]
    return messageList

#Narrative: Allows for the one player game to be played - click cards and match
#pairs together. Displays score as user goes along. Go back to menu by button
#PreConditions: Name of player, theme of card and set of card must be passed in
#PostConditions: Displays final score, allows user to go back to main menu, adds
#player to highscore file.
def game(player1, themeType, cardSetType):
    pygame.init()

    title = pygame.image.load("Pictures/title.png")
    left = pygame.image.load("Pictures/left.png")
    blueSquare = pygame.image.load("Pictures/blueSquare.png")
    blueSquare2 = pygame.image.load("Pictures/blueSquare2.png")

    imageList = imageCheck.imageGet()
    sports = imageList[0]
    animals = imageList[1]
    cars = imageList[2]

#Checks to see the value of cardSetType that was passed in, then sets the set
    if cardSetType == "Sports":
        cardSet = sports
    elif cardSetType == "Animals":
        cardSet = animals
    else:
        cardSet = cars

    clouds = pygame.image.load("Pictures/Themes/Clouds.png")
    glass = pygame.image.load("Pictures/Themes/Glass.png")
    question = pygame.image.load("Pictures/Themes/Question.png")
    questionScrollOver = pygame.image.load\
                         ("Pictures/Themes/QuestionScrollOver.png")
    cloudsScrollOver = pygame.image.load\
                       ("Pictures/Themes/CloudsScrollOver.png")
    glassScrollOver = pygame.image.load\
                       ("Pictures/Themes/GlassScrollOver.png")

#Checks to see the value of themeType that was passed in, then sets the theme
    if themeType == "Questions":
        theme = question
        themeScrollOver = questionScrollOver
    elif themeType == "Clouds":
        theme = clouds
        themeScrollOver = cloudsScrollOver
    else:
        theme = glass
        themeScrollOver = glassScrollOver

    displayWidth = 800
    displayHeight = 600

    black = (0, 0, 0) 
    white = (255, 255, 255)
    blue = (0, 128, 255)
    purple = (102, 51, 153)

    font1 = pygame.font.SysFont(None,23)

    gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

#Displays back button
    back = Button.Button(gameDisplay, blue, white, (50,535),(255,50),\
                         "Main Menu",purple)
    back.drawButton()

    totalPointsText = (player1.title() + "'s Total Points")
    
    gameDisplay.fill(blue)
    gameDisplay.blit(title,(245,5))

#Displays "TotalPoints:" text
    messageOne = font1.render(totalPointsText,1,white)
    gameDisplay.blit(messageOne,(5,25))

#Displays amount of points needed to win
    messageTwo = font1.render("Match All 12 Pairs To Win!",10,white)
    gameDisplay.blit(messageTwo,(330,535))

#Gets the message list for displaying the amount of points left
    messageList = getMessageList(font1,white)
#Displays the hand for the player turn, in this case only towards player1
    gameDisplay.blit(left,(190,20))

#Makes the cards inside of a different module
    cardList2 = getCards.getCards(gameDisplay,cardSet,theme,themeScrollOver)
    for card in cardList2:
        card.drawButton()
    pygame.time.wait(1000)
    for card in cardList2:
        card.drawCardImage()
    pygame.time.wait(2500)
    for card in cardList2:
        card.drawButton()

#Sets the click count to zero so game starts fresh, points to zero, time 0, etc
    clickCount = 0
    cardList = []
    running = True
    playerOnePoints = 0
    scored = 0
    timer = 0
    clock = pygame.time.Clock()
    timerFont = pygame.font.SysFont("century", 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#begins the timer
        seconds = clock.tick()
#As long as game is still being played, timer keeps going
        if playerOnePoints < 12:
            timer += seconds
        timerText = timerFont.render("Timer: " + format(timer/1000.0, '.3f'),\
                                     True, black)
#Displays timer on the game display
        gameDisplay.blit(blueSquare,(570,10))
        gameDisplay.blit(timerText, (560,10))

        if d.buttonDetect(back):
            running = False

        for card in cardList2:
            if not card.getClicked():
                if d.buttonDetect(card):
                    card.drawCardImage()
                    card.setClicked(True)
                    cardList.append(card)
                    clickCount += 1

#Updates the score each time after 2 clicks, checks to see if images match to
#give the value of points either 0 or 1
        if clickCount==2:
            points = 0
                
            pygame.time.wait(1000)
            cardList[0],cardList[1],points=imageCheck.imageCheck\
                                             (cardList[0],\
                                              cardList[1],points)

            playerOnePoints += points
            scoreOne = font1.render(str(playerOnePoints),1,white)
            gameDisplay.blit(blueSquare2, (83,44))
            gameDisplay.blit(scoreOne,(83,50))

#Clears the list in order to add more to check after the end of the turn
            clickCount = 0
            cardList.clear()
            pygame.time.wait(50)
            gameDisplay.blit(blueSquare,(560,534))
            gameDisplay.blit(messageList[playerOnePoints],(560,535))
#After the game ends:
        if playerOnePoints == 12 and scored == 0:
# This is to ensure that even if two people get the same time, they
# will have different dictionary values. It has no effect but separates values
            timerEnd = timer*100 + random.randint(1,45)
#opens highscores
            try:
                highscores = pickle.load(open("highscoresList.dat",'rb'))
            except:
                highscores = {}
            highscores[str(timerEnd)] = str(player1)
#saves the  highscores as a dictionary with key being time, value being name
            try:
                pickle.dump(highscores,open("highscoresList.dat",'wb'))
            except:
                pass
            scored += 1
