import Deck

# Create deck for game

deck = Deck.Deck()

# Create hands
hand_player = []
hand_dealer = []


def deal(hand_player, hand_dealer):
    hand_player.append(deck.deal_card())
    hand_dealer.append(deck.deal_card())
    return hand_player, hand_dealer


def show_hand(hand_player, hand_dealer):
    print ("Your Hand:")
    totals = [0]
    for card in hand_player:
        print(card.get_card())
        for idx, total in enumerate(totals):
            if card.get_value() != 0:
                totals[idx] += card.get_value()
            else:
                totals.append(totals[idx]+10)
                totals[idx] += 1
                break
    print(totals)


def get_user_cont():
    print ("""Hit or Stand:
    1. Hit
    2. Stand""")
    cont = input("Please enter your choice:")
    if cont == 1:
        return True
    elif cont == 2:
        return False
    else:
        print ("That is not a valid input")


def game_turn(hand_player, hand_dealer):
    hit = True
    if hit:
        hand_player, hand_dealer = deal(hand_player, hand_dealer)
        show_hand(hand_player, hand_dealer)
        hit = get_user_cont()


#
# for i in range(2):
#     hand_player, hand_dealer = deal(hand_player, hand_dealer)
#
# show_hand(hand_player,hand_dealer)
