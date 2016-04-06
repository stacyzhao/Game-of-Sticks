
import random
import sys

def starting_number_sticks():
    while True:
        sticks = input("How many sticks do you want to start with? ")
        if sticks == "":
            print("Looks like you didn't give me a number. Try again.")
            continue
        try:
            int(sticks)
            return int(sticks)
        except:
            print("Looks like you didn't give me a whole number. Try again.")
            continue

def user_picks_sticks():
    while True:
        player1 = input("How many sticks do you want to pick up from the table (1-3)? \n")
        if player1 == "":
            print("Looks like you didn't give me a number. Try again.")
            continue
        elif player1 == '0':
            print("Your number of sticks needs to be more than 0. Try again.")
            continue
        try:
            int(player1)
            return int(player1)
        except:
            print("Looks like you didn't give me a whole number. Try again.")
            continue
        if int(player1) > 3 or int(player1) < 1:
            print ("Looks like you didn't give me a number from 1 to 3. Try again.")
            continue

def determine_turn(number_of_turns):
    if number_of_turns % 2 == 1:
        #user turn
        return True
    elif number_of_turns % 2 == 0:
        #AI turn
        return False

def play_again():
    "Asks user if they want to play the game again."

    play_again = input("Do you want to play Game of Sticks again? [y/N] \n")

    if play_again.lower().strip() == "y":
        main()

    else:
        sys.exit()

def determine_turn(number_of_turns):
    if number_of_turns % 2 == 1:
        #user turn
        return True
    elif number_of_turns % 2 == 0:
        #AI/Player2 turn
        return False

def main():
    total_number_sticks = 0
    number_of_turns = 1

    print ("Welcome to the Game of Sticks!")

    while True:
        total_number_sticks = starting_number_sticks()
        while total_number_sticks > 0:
            print("There are {} sticks on the board.".format(total_number_sticks))
            if determine_turn(number_of_turns):
                total_number_sticks -= user_picks_sticks()
            else:
                total_number_sticks -= user_picks_sticks()
                print("Player2 picked {} stick(s).".format(total_number_sticks))

            number_of_turns += 1

        else:
            # user loses
            if determine_turn(number_of_turns) == True:
                print ("Player1 Loses")
            # AI/Player2 loses
            else:
                print ("Player2 Loses")

            play_again()

if __name__ == '__main__':
    main()
