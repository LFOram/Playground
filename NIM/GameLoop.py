

def main_loop(dif):
    #initialise new game
    remaining = 12
    while (True):
        #User turn
        to_remove = get_user_move(remaining)
        if to_remove == -1:
            exit()
        remaining -= to_remove
        print("Removed " + str(to_remove) + ", "+ str(remaining) +" remain.")
        if remaining == 0:
            print("0 Remain! You Lose!")
            return
        #AI turn
        #if dif == 1:#easy
           #easymode()



def get_user_move(remain):
    options =[-1,1,2,3]
    while(True):
        try:
            user_input = int(input("Please make your move (-1 to quit):"))
            if user_input in options and user_input <= remain:
                return user_input
            else:
                print("Invalid input5")
        except ValueError:
            print("Invalid Input")


main_loop(1)