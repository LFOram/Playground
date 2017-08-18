class Card():
    suit = None
    value = None

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return ("The " + self.value + " of " + self.suit)

