class Card():
    suit = None
    value = None

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return ("The " + self.value + " of " + self.suit)

def create_deck():
    suits = ["Hearts","Clubs","Diamonds","Spades"]
    values = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    #create deck
    deck = []
    for suit in suits:
        for value in values:
            card = Card(suit,value)
            deck.append(card)
    return deck

if __name__ == '__main__':
    deck = create_deck()
    for card in deck:
        print(card.get_card())
