import Deck
import Blackjack


def options_menu():
    # User interface to select game to play
    options = [-1, 1]
    while True:  # input validation
        print ('''Please select a game to play:
                 1. Blackjack
                -1. Quit''')
        u_input = input("Enter a number to select:")
        if u_input in options:  # Leave loop if valid option.
            return u_input
        else:  # Invalid input
            print ("Please select a valid option")


def start_game(choice):
    # Python "case/switch statement.
    # used instead of a if/elseif/else block to improve readability
    options = {1: blackjack,
               -1: close}
    options[choice]()


def blackjack():
    Blackjack.start(Deck)


def close():
    print ("Thanks for playing!")
    quit()


if __name__ == "__main__":
    # create a  deck
    new_deck = Deck.deck()
    # Display interface
    game = options_menu()
    # Select game through switch block nad start game or quit
    start_game(game)
