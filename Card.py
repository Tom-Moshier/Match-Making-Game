# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame

class Card():
    def __init__(self, screen, rectCords, rectSize, background, \
                 scrollOver, cardImage, clicked):
        self.__screen = screen
        self.__rectCords = rectCords
        self.__rectSize = rectSize
        self.__background = background
        self.__scrollOver = scrollOver
        self.__cardImage = cardImage
        self.__clicked = clicked

    # Narrative: Gets rectangular coordinates of the card
    # Precondition: Must be called
    # Postcondition: Returned the list of rectangle coordinates
    def getRectCords(self):
        return self.__rectCords

    # Narrative: Gets rectangular size of the card
    # Precondition: Must be called
    # Postcondition: Returned the list of rectangle size
    def getRectSize(self):
        return self.__rectSize

    # Narrative: Sets click state
    # Precondition: Must be called and receive clicked state
    # Postcondition: Set click state locally
    def setClicked(self,clicked):
        self.__clicked = clicked

    # Narrative: Gets click state of the card
    # Precondition: Must be called
    # Postcondition: Returned the click state of the card
    def getClicked(self):
        return self.__clicked

    # Narrative: Gets the image of the card
    # Precondition: Must be called
    # Postcondition: Returned the image of the card
    def getCardImage(self):
        return self.__cardImage

    # Narrative: Sets the default picture of the card
    # Precondition: must be called and receive a picture
    # Postcondition: Set the default picture locally
    def setBackground(self, background):
        self.__background = background

    # Narrative: Sets the scroll over picture of the card
    # Precondition: Must be called and receive a picture
    # Postcondition: Set the scroll over picture locally
    def setScrollOver(self, scrollOver):
        self.__scrollOver = scrollOver

    # Narrative: set the card clicked picture
    # Precondition: Must be called and receive a picture
    # Postcondition: Set the clicked card picture locally
    def setCardImage(self,cardImage):
        self.__cardImage = cardImage

    # Narrative: Draws the default state of the card onto the screen
    # Precondition: Must be called
    # Postcondition: Drew the card and updated the display
    def drawButton(self):
        self.__screen.blit(self.__background, self.__rectCords)
        pygame.display.update()

    # Narrative: Draws the scrollover state of the card onto the screen
    # Precondition: Must be called
    # Postcondition: Drew the card and updated the display
    def drawButtonActive(self):
        self.__screen.blit(self.__scrollOver, self.__rectCords)
        pygame.display.update()

    # Narrative: Draws the clicked value of the card onto the screen
    # Precondition: Must be called
    # Postcondition: Drew the card and updated the display
    def drawCardImage(self):
        self.__screen.blit(self.__cardImage, self.__rectCords)
        pygame.display.update()

    def __str__(self):
        return "Rectangle Coordinates: " + str(self.__rectCords) +\
               "\nRectangle Size: " + str(self.__rectSize) + \
               "\n Click State: " + str(self.__clicked)
