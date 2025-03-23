import os
import re


playing = True

spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

choices = []

def restart_game():
    play_again = input("Would you play again yes or no?")
    if play_again.lower() == "yes":
        for i in range(9):
            spots[i+1] = str(i+1)
        choices.clear()
        game_loop()


    elif play_again.lower() == "no":
        print("Thanks for playing!")
        exit()

def check_victory(spots, turn):
    if spots[1] == spots[2] == spots[3]:
        print(draw_board(spots))
        return spots[1] or None
    elif spots[4] == spots[5] == spots[6]:
        print(draw_board(spots))
        return spots[4] or None
    elif spots[7] == spots[8] == spots[9]:
        print(draw_board(spots))
        return spots[7] or None
    elif spots[1] == spots[4] == spots[7]:
        print(draw_board(spots))
        return spots[1] or None
    elif spots[2] == spots[5] == spots[8]:
        print(draw_board(spots))
        return spots[2] or None
    elif spots[3] == spots[6] == spots[9]:
        print(draw_board(spots))
        return spots[3] or None
    elif spots[1] == spots[5] == spots[9]:
        print(draw_board(spots))
        return spots[1] or None
    elif spots[3] == spots[5] == spots[7]:
        print(draw_board(spots))
        return spots[3] or None
    elif turn == 9:
        print(draw_board(spots))
        return "Draw"


def check_input(choice):
    while True:
        if choice.lower() == 'q':
            print("Thanks for playing!")
            exit()  # Exit the program

        if choice in choices:
            print("Number allready choosen, choose another number")
            choice = input("Please choose a number between 1 and 9 or 'q' to quit the game: ")
            continue

        if not re.match("^[1-9]$", choice):
            choice = input("Please choose a number between 1 and 9 or 'q' to quit the game: ")
            continue

        return choice

def play_turn(number):
    if number % 2 == 0:
        return "O"
    else:
        return "X"

def draw_board(spots):
    board = f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|\n"
    return board

def game_loop():
    turn = 0
    while True:
        print(draw_board(spots))
        turn += 1
        player = play_turn(turn)
        choice = input(f"Player {play_turn(turn)}, choose number between 1 and 9 or q to quit the game: ")
        choice = check_input(choice)
        choices.append(choice)
        # turn += 1
        # player = play_turn(turn)
        spots[int(choice)] = player
        sign_victory = check_victory(spots, turn)
        if sign_victory != None and sign_victory != "Draw":
            print(f"Player {sign_victory} won")
            restart_game()
            exit()
        elif sign_victory == 'Draw': 
            print("Draw")
            restart_game()

game_loop()
