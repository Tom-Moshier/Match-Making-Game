# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import sys

pygame.init()

class Button:
    def __init__(self,screen,rectColorReg,rectColorActive,rectCords,rectSize,\
                 text,background):
        self.__textObject = pygame.font.SysFont("Times New Roman, Arial",53)
        self.__text = text
        self.__textDraw = self.__textObject.render(self.__text,True,(0,0,0))
        self.__screen = screen
        self.__rectColorReg = rectColorReg
        self.__rectColorActive = rectColorActive
        self.__rectCords = rectCords
        self.__rectSize = rectSize
        self.__textCords = (rectCords[0]+3,rectCords[1]-5)
        self.__background = background

    # Narrative: Draws the button and corresponding text onto the screen
    # Precondition: Must be called
    # Postcondition: Drew the button and updated the display
    def drawButton(self):
        self.__screen.lock()
        pygame.draw.rect(self.__screen,self.__rectColorReg,\
                         pygame.Rect(self.__rectCords,self.__rectSize))
        self.__screen.unlock()
        self.__screen.blit(self.__textDraw,self.__textCords)
        pygame.display.update()

    # Narrative: Draws the button and corresponding text onto the screen with
    # the color for when the button is being scrolled over
    # Precondition: Must be called
    # Postcondition: Drew the scrolled over form of the button and updated
    # the display
    def drawButtonActive(self):
        self.__screen.lock()
        pygame.draw.rect(self.__screen,self.__rectColorActive,\
                         pygame.Rect(self.__rectCords,self.__rectSize))
        self.__screen.unlock()
        self.__screen.blit(self.__textDraw,self.__textCords)
        pygame.display.update()

    # Narrative: Draws the button with the background color to make it
    # disappear
    # Precondition: Must be called
    # Postcondition: Covered the previous instance of button to hide it and
    # updated display
    def drawButtonCover(self):
        self.__screen.lock()
        pygame.draw.rect(self.__screen,self.__background,\
                         pygame.Rect(self.__rectCords,self.__rectSize))
        self.__screen.unlock()
        pygame.display.update()

    # Narrative: Draws the button text in its correct location
    # Precondition: Must be called
    # Postcondition: Drew the button text without the button
    def drawText(self):
        self.__screen.blit(self.__textDraw,self.__textCords)
        pygame.display.update()

    # Narrative: Gets rectangular coordinates of the button
    # Precondition: Must be called
    # Postcondition: Returned the list of rectangle coordinates
    def getRectCords(self):
        return self.__rectCords

    # Narrative: Gets rectangular size of the button
    # Precondition: Must be called
    # Postcondition: Returned the list of rectangle size
    def getRectSize(self):
        return self.__rectSize

    # Narrative: Sets text
    # Precondition: Must be called and receive text
    # Postcondition: Set text locally
    def setText(self,text):
        self.__text = text

    # Narrative: Sets text draw
    # Precondition: Must be called
    # Postcondition: Set text draw locally
    def setTextDraw(self):
        self.__textDraw = self.__textObject.render(self.__text,True,(0,0,0))

    # Narrative: Gets the button's text
    # Precondition: Must be called
    # Postcondition: Returned the text value
    def getText(self):
        return self.__text 

    def __str__(self):
        return "Text: "+ self.__text + "\nRegular Rectangular Color: "+\
               str(self.__rectColorReg) + "\n Scrollover Rectangular Color: "+\
               str(self.__rectColorActive) + "\nRectangle Coordinates: " +\
               str(self.__rectCords) + "\nRectangle Size: " +\
               str(self.__rectSize) + "\nRectangle Hide Color: " +\
               str(self.__background)
