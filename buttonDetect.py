# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame

# Narrative: Checks if the button is being hovered over or clicked
# Precondition: Must be called and receive a rectangular object
# Postcondition: Checked if the cursor was clicked within the boundaries
# of the object. If yes, returned True. Otherwise, False.
def buttonDetect(button):
    pressed = False
    x, y = pygame.mouse.get_pos()
    buttonXOne = button.getRectCords()[0]
    buttonXTwo = buttonXOne + button.getRectSize()[0]
    buttonYOne = button.getRectCords()[1]
    buttonYTwo = buttonYOne + button.getRectSize()[1]

    if x>buttonXOne and x<buttonXTwo and y>buttonYOne and y<buttonYTwo:
        button.drawButtonActive()
        if pygame.mouse.get_pressed()[0]:
            pressed = True
    else:
         button.drawButton()

    return pressed
