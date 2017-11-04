import Cards
import random

class Deck():
    def __init__(self):
        self.deck = self.new_deck()

    def create_deck(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        deck = []
        #create deck

        for suit in suits:
            for value in values:
                card = Cards.Card(suit, value)
                deck.append(card)
        return deck

    def shuffle(self,deck):
        shuffled = []
        print("shuffle")
        while deck != []:
            rand = random.randint(0, len(deck)-1)
            shuffled.append(deck[rand])
            deck.pop(rand)
        return shuffled

    def new_deck(self):
        deck = self.create_deck()
        for i in range(7):
            deck = self.shuffle(deck)
        #for card in deck:
            #print(card.get_card())
        return deck

    def deal_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card