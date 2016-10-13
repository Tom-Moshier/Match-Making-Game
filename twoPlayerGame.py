# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button
import buttonDetect as d
import sys
import imageCheck
import getCards

#Narrative: Allows for the two player game to be played - click cards and match
#pairs together. Displays score as user goes along. Go back to menu by button
#PreConditions: Name of player, theme of card and set of card must be passed in
#PostConditions: Displays final score, allows user to go back to main menu
def game(player1, player2,themeType,cardSetType):
    title = pygame.image.load("Pictures/title.png")
    left = pygame.image.load("Pictures/left.png")
    right = pygame.image.load("Pictures/right.png")
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

    white = (255, 255, 255)
    blue = (0, 128, 255)
    purple = (102, 51, 153)

    font1 = pygame.font.SysFont(None,23)

    gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
    gameDisplay.fill(blue)
    gameDisplay.blit(title,(254,5))
    gameDisplay.blit(left,(190,20))
    totalPointsText1 = (player1.title() + "'s Total Points")
    totalPointsText2 = (player2.title() + "'s Total Points")

#All of the messages for the score
    messageFour = font1.render(player1.title()+" WINS!!!",30,white)
    messageFive = font1.render(player2.title()+" WINS!!!",30,white)
    messageSix = font1.render("Draw! No One Wins.",30,white)
    messageSeven = font1.render\
                   (player1.title()+" is Currently Winning!",10,\
                    white)
    messageEight = font1.render\
                   (player2.title() +" is Currently Winning!",10,\
                    white)
    messageNine = font1.render("The Game is Tied...",10,white)
    
#Displays the users names 
    messageOne = font1.render(totalPointsText1,1,white)
    messageTwo = font1.render(totalPointsText2,10,white)
    gameDisplay.blit(messageOne,(5,25))
    gameDisplay.blit(messageTwo,(625,25))

#Displays the amount of points it takes to win
    messageThree = font1.render("First To 7 Points Wins",10,white)
    gameDisplay.blit(messageThree,(330,535))

#MainMenu button
    back = Button.Button(gameDisplay, blue, white, (50,535),(255,50),\
                         "Main Menu",purple)
    back.drawButton()

#Gets the card
    cardList2 = getCards.getCards(gameDisplay,cardSet,theme,themeScrollOver)

#Sets the click count to zero so game starts fresh, points to zero, time 0, etc    
    clickCount = 0
    cardList = []
    running = True
    playerTurn = 1
    playerOnePoints = 0
    playerTwoPoints = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
#If main menu is clicked entire game stops and exits the module
        if d.buttonDetect(back):
            running = False

        for card in cardList2:
            if not card.getClicked():
                if d.buttonDetect(card):
                    card.drawCardImage()
                    card.setClicked(True)
                    cardList.append(card)
                    clickCount += 1

#If any player gets more than 6 points the game ends because they won. You are
#Then able to click all the cards to reveal them as it will no longer check if
#They are pairs
        if playerOnePoints <=6 and playerTwoPoints <=6:
            if clickCount==2:
                points = 0
                    
                pygame.time.wait(1000)
                cardList[0],cardList[1],points=\
                                                 imageCheck.imageCheck\
                                                 (cardList[0],\
                                                  cardList[1],points)
#Changes user turns and placement of the hand which shows whose turn it is
                if playerTurn == 1:
                    playerOnePoints += points
                    playerTurn = 2
                    gameDisplay.blit(right,(575,30))
                    gameDisplay.blit(blueSquare2, (190,26))
                else:
                    playerTwoPoints += points
                    playerTurn = 1
                    gameDisplay.blit(left,(190,20))
                    gameDisplay.blit(blueSquare2,(575,27))

#Clears the list in order to add more to check after the end of the turn        
                clickCount = 0
                cardList.clear()
                pygame.time.wait(50)

                scoreOne = font1.render(str(playerOnePoints),1,white)
                scoreTwo = font1.render(str(playerTwoPoints),1,white)

                gameDisplay.blit(blueSquare2,(83,44))
                gameDisplay.blit(scoreOne,(83,50))
                gameDisplay.blit(blueSquare2,(717,44))
                gameDisplay.blit(scoreTwo,(717,50))

#At the end of each turn, updates the scores: displays them
                if playerOnePoints == 7:
                    gameDisplay.blit(blueSquare,(560,536))
                    gameDisplay.blit(messageFour,(570, 535))
                elif playerTwoPoints == 7:
                    gameDisplay.blit(blueSquare,(560,536))
                    gameDisplay.blit(messageFive,(570,535))
                elif playerTwoPoints == 6 and playerOnePoints == 6:
                    gameDisplay.blit(blueSquare,(560,536))
                    gameDisplay.blit(messageSix,(570,535))
                elif playerTwoPoints > playerOnePoints:
                    gameDisplay.blit(blueSquare,(560,536))
                    gameDisplay.blit(messageEight,(570,535))
                elif playerOnePoints > playerTwoPoints:
                    gameDisplay.blit(blueSquare,(560,536))
                    gameDisplay.blit(messageSeven,(570,535))
                else:
                    gameDisplay.blit(blueSquare,(560,536))
                    gameDisplay.blit(messageNine,(570,535))
