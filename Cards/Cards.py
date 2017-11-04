class Card():
    suit = None
    value = None

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def get_card(self):
        return ("The " + self.value + " of " + self.suit)

    def get_value(self):
        if self.value == "Ace":
            return 0 #0=ace// 1 or 11
        elif self.value == "Two":
            return 2
        elif self.value == "Three":
            return 3
        elif self.value == "Four":
            return 4
        elif self.value == "Five":
            return 5
        elif self.value == "Six":
            return 6
        elif self.value == "Seven":
            return 7
        elif self.value == "Eight":
            return 8
        elif self.value == "Nine":
            return 9
        else:
            return 10


