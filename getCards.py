# Moshier, Thomas; Chellis, Andrew; Hector, Billy
# CS 110, A51, A53, A51
# Project

import Card
import random

# Narrative: Makes the list of cards for the game and assigns each a random
# picture
# Precondition: Must receive gameDisplay, cardSet, theme and themeScrollOver
# Postcondition: Returned a list of cards with randomly assigned pictures to
# make a new, random game board
def getCards(gameDisplay,cardSet,theme,themeScrollOver):
    cardsRandom = []
    cards = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11]
    for i in range(24):
        randomCard = cards[random.randint(0 ,len(cards) -1)]
        cardsRandom.append(randomCard)
        cards.remove(randomCard)

    card1 = Card.Card(gameDisplay,(56,83),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[0]],False)
    card2 = Card.Card(gameDisplay,(172,83),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[1]],False)
    card3 = Card.Card(gameDisplay,(288,83),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[2]],False)
    card4 = Card.Card(gameDisplay,(404,83),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[3]],False)
    card5 = Card.Card(gameDisplay,(520,83),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[4]],False)
    card6 = Card.Card(gameDisplay,(636,83),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[5]],False)
    card7 = Card.Card(gameDisplay,(56,194),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[6]],False)
    card8 = Card.Card(gameDisplay,(172,194),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[7]],False)
    card9 = Card.Card(gameDisplay,(288,194),(109,104),theme,\
                      themeScrollOver,cardSet[cardsRandom[8]],False)
    card10 = Card.Card(gameDisplay,(404,194),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[9]],False)
    card11 = Card.Card(gameDisplay,(520,194),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[10]],False)
    card12 = Card.Card(gameDisplay,(636,194),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[11]],False)
    card13 = Card.Card(gameDisplay,(56,305),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[12]],False)
    card14 = Card.Card(gameDisplay,(172,305),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[13]],False)
    card15 = Card.Card(gameDisplay,(288,305),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[14]],False)
    card16 = Card.Card(gameDisplay,(404,305),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[15]],False)
    card17 = Card.Card(gameDisplay,(520,305),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[16]],False)
    card18 = Card.Card(gameDisplay,(636,305),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[17]],False)
    card19 = Card.Card(gameDisplay,(56,416),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[18]],False)
    card20 = Card.Card(gameDisplay,(172,416),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[19]],False)
    card21 = Card.Card(gameDisplay,(288,416),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[20]],False)
    card22 = Card.Card(gameDisplay,(404,416),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[21]],False)
    card23 = Card.Card(gameDisplay,(520,416),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[22]],False)
    card24 = Card.Card(gameDisplay,(636,416),(109,104),theme,\
                       themeScrollOver,cardSet[cardsRandom[23]],False)

    cardList2 = [card1,card2,card3,card4,card5,card6,card7,card8,card9,\
                 card10,card11,card12,card13,card14,card15,card16,card17,\
                 card18,card19,card20,card21,card22,card23,card24]
    return cardList2
