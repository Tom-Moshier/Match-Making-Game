# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import pygame

# Narrative: Checks if two cards are matches
# Precondition: Must receive two cards and points
# Postcondition: Checked if two cards were matches to
#  determine if user got a point
def imageCheck(card1,card2,points):
    if card1.getCardImage() != card2.getCardImage():
        card1.setClicked(False)
        card2.setClicked(False)
        points = 0
    else:
        points = 1
    return [card1,card2,points]

# Narrative: Gets the different sets of images for the game
# Precondition: Must be called
# Postcondition: Returned a list containing the three lists of pictures for
# the game
def imageGet():
    sports = [pygame.image.load("Pictures/Sports/archery.png"),\
          pygame.image.load("Pictures/Sports/baseball.png"),\
          pygame.image.load("Pictures/Sports/basketball.png"),\
          pygame.image.load("Pictures/Sports/boxing.png"),\
          pygame.image.load("Pictures/Sports/fishing.png"),\
          pygame.image.load("Pictures/Sports/football.png"),\
          pygame.image.load("Pictures/Sports/hockey.png"),\
          pygame.image.load("Pictures/Sports/running.png"),\
          pygame.image.load("Pictures/Sports/soccer.png"),\
          pygame.image.load("Pictures/Sports/tennis.png"),\
          pygame.image.load("Pictures/Sports/weights.png"),\
          pygame.image.load("Pictures/Sports/volleyball.png")]

    animals = [pygame.image.load("Pictures/Animals/bear.png"),\
          pygame.image.load("Pictures/Animals/dolphin.png"),\
          pygame.image.load("Pictures/Animals/donkey.png"),\
          pygame.image.load("Pictures/Animals/elephant.png"),\
          pygame.image.load("Pictures/Animals/frog.png"),\
          pygame.image.load("Pictures/Animals/giraffe.png"),\
          pygame.image.load("Pictures/Animals/lion.png"),\
          pygame.image.load("Pictures/Animals/monkey.png"),\
          pygame.image.load("Pictures/Animals/penguin.png"),\
          pygame.image.load("Pictures/Animals/rabbit.png"),\
          pygame.image.load("Pictures/Animals/shark.png"),\
          pygame.image.load("Pictures/Animals/tiger.png")]

    cars = [pygame.image.load("Pictures/Cars/car1.png"),\
          pygame.image.load("Pictures/Cars/car2.png"),\
          pygame.image.load("Pictures/Cars/car3.png"),\
          pygame.image.load("Pictures/Cars/car4.png"),\
          pygame.image.load("Pictures/Cars/car5.png"),\
          pygame.image.load("Pictures/Cars/car6.png"),\
          pygame.image.load("Pictures/Cars/car7.png"),\
          pygame.image.load("Pictures/Cars/car8.png"),\
          pygame.image.load("Pictures/Cars/car9.png"),\
          pygame.image.load("Pictures/Cars/car10.png"),\
          pygame.image.load("Pictures/Cars/car11.png"),\
          pygame.image.load("Pictures/Cars/car12.png")]

    return [sports,animals,cars]
