import Cards
import random


def create_deck():
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    deck = []
    #create deck

    for suit in suits:
        for value in values:
            card = Cards.Card(suit, value)
            deck.append(card)
    return deck

def shuffle(deck):
    shuffled = []
    print("shuffle")
    while deck != []:
        rand = random.randint(0, len(deck)-1)
        shuffled.append(deck[rand])
        deck.pop(rand)
    return shuffled

def deck():
    deck = create_deck()
    for i in range(7):
        deck = shuffle(deck)
    #for card in deck:
        #print(card.get_card())
    return deck