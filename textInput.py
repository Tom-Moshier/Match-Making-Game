# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame
import Button

# Narrative: Gets user text input by reading each key
# Precondition: Must receive the screen and a button to display text on
# Postcondition: Returned text input consisting of text or number input
def textInput(screen,b1):
    inputString = []
    wait = 0
    enter = True
    
    while enter:
        name = ""
        preLength = len(inputString)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                wait = 90
                if event.key == pygame.K_0:
                    inputString.append("0")
                elif event.key == pygame.K_1:
                    inputString.append("1")
                elif event.key == pygame.K_2:
                    inputString.append("2")
                elif event.key == pygame.K_3:
                    inputString.append("3")
                elif event.key == pygame.K_4:
                    inputString.append("4")
                elif event.key == pygame.K_5:
                    inputString.append("5")
                elif event.key == pygame.K_6:
                    inputString.append("6")
                elif event.key == pygame.K_7:
                    inputString.append("7")
                elif event.key == pygame.K_8:
                    inputString.append("8")
                elif event.key == pygame.K_9:
                    inputString.append("9")
                elif event.key == pygame.K_q:
                    inputString.append("q")
                elif event.key == pygame.K_w:
                    inputString.append("w")
                elif event.key == pygame.K_e:
                    inputString.append("e")
                elif event.key == pygame.K_r:
                    inputString.append("r")
                elif event.key == pygame.K_t:
                    inputString.append("t")
                elif event.key == pygame.K_y:
                    inputString.append("y")
                elif event.key == pygame.K_u:
                    inputString.append("u")
                elif event.key == pygame.K_i:
                    inputString.append("i")
                elif event.key == pygame.K_o:
                    inputString.append("o")
                elif event.key == pygame.K_p:
                    inputString.append("p")
                elif event.key == pygame.K_a:
                    inputString.append("a")
                elif event.key == pygame.K_s:
                    inputString.append("s")
                elif event.key == pygame.K_d:
                    inputString.append("d")
                elif event.key == pygame.K_f:
                    inputString.append("f")
                elif event.key == pygame.K_g:
                    inputString.append("g")
                elif event.key == pygame.K_h:
                    inputString.append("h")
                elif event.key == pygame.K_j:
                    inputString.append("j")
                elif event.key == pygame.K_k:
                    inputString.append("k")
                elif event.key == pygame.K_l:
                    inputString.append("l")
                elif event.key == pygame.K_z:
                    inputString.append("z")
                elif event.key == pygame.K_x:
                    inputString.append("x")
                elif event.key == pygame.K_c:
                    inputString.append("c")
                elif event.key == pygame.K_v:
                    inputString.append("v")
                elif event.key == pygame.K_b:
                    inputString.append("b")
                elif event.key == pygame.K_n:
                    inputString.append("n")
                elif event.key == pygame.K_m:
                    inputString.append("m")
                elif event.key == pygame.K_RETURN:
                    enter = False
                elif event.key == pygame.K_BACKSPACE:
                    if len(inputString)>0:
                        b1.drawButtonCover()
                        del inputString[-1]
                else:
                    wait = 0
            pygame.event.clear()
        if preLength != len(inputString):
            # This is used to limit the length of the user name input
            # If the user types at ludicrously fast speeds, it will rollover
            # This is our best attempt to stop that
            if len(inputString)>7:
                num = 6
                while num <100:
                    try:
                        del inputString[num]
                        num += 1
                    except:
                        num = 101
            for element in inputString:
                name += element
            b1.setText(name.title())
            b1.setTextDraw()
        b1.drawButton()
        pygame.time.wait(wait)
    return b1
