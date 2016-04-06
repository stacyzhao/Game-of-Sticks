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
        player1 = input("How many sticks do you want to pick up from the table (1-3)? ")
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

def ai_picks_sticks(current_number_sticks, game_dict, ai_dict):
    ai_sticks = random.choice(game_dict[current_number_sticks])
    ai_dict[current_number_sticks] = ai_sticks
    return ai_sticks

def ai_wins(total_number_sticks):
    if total_number_sticks == 3:
        return 2
    if total_number_sticks == 2:
        return 1
    if total_number_sticks == 1:
        return 1

def play_again():
    "Asks user if they want to play the game again."

    play_again = input("Do you want to play Game of Sticks again? [y/N] \n")

    if play_again.lower().strip() == "y":
        main()

    else:
        sys.exit()

# def game_option():
#     option = int(input("""Option: \n
#         Play against a friend (1) \n
#         Play against the computer (2) \n
#         Which option do you take (1-2)?"""))
#
#     if option == 1:
#         play against a friend
    # else:
        #play against a computer

def update_dict(game_dict, ai_dict):
    for k in ai_dict:
        print("k", k)
        game_dict[k].append(ai_dict[k])


def main():
    total_number_sticks = 0
    number_of_turns = 1

    game_dict = {}
    ai_dict = {}

    print ("Welcome to the Game of Sticks! \n")

    while True:
        total_number_sticks = starting_number_sticks()
        game_dict = {n: [1,2,3] for n in range(1,total_number_sticks)}
        while total_number_sticks > 0:
            print("There are {} sticks on the board. \n".format(total_number_sticks))
            if determine_turn(number_of_turns):
                total_number_sticks -= user_picks_sticks()
            else:
                ai_sticks = ai_picks_sticks(total_number_sticks, game_dict, ai_dict)
                total_number_sticks -= ai_sticks
                print("AI picked {} stick(s). \n".format(ai_sticks))
            number_of_turns +=1

        else:
            # user loses
            if determine_turn(number_of_turns) == True:
                update_dict(game_dict, ai_dict)
                print ("user end game dict: ", game_dict)
                print ("User Loses")
            # ai loses
            else:
                ai_dict.clear()
                print ("ai end game dict: ", game_dict)
                print ("AI Loses")
            play_again()

if __name__ == '__main__':
    main()
