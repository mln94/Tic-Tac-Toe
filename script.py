import os
import re


playing = True

spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

choices = []

def restart_game():
    play_again = input("Would you play again yes or no? ")
    global spots
    if play_again.lower() == "yes":
        spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        choices.clear()
        game_loop()
    elif play_again.lower() == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        restart_game()

def check_victory(spots, turn):
    if spots[1] == spots[2] == spots[3]:
        return spots[1]
    elif spots[4] == spots[5] == spots[6]:
        return spots[4]
    elif spots[7] == spots[8] == spots[9]:
        return spots[7]
    elif spots[1] == spots[4] == spots[7]:
        return spots[1]
    elif spots[2] == spots[5] == spots[8]:
        return spots[2]
    elif spots[3] == spots[6] == spots[9]:
        return spots[3]
    elif spots[1] == spots[5] == spots[9]:
        return spots[1]
    elif spots[3] == spots[5] == spots[7]:
        return spots[3]
    elif turn == 9:
        return "Draw"
    return None


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
        choice = input(f"Player {player}, choose number between 1 and 9 or q to quit the game: ")
        choice = check_input(choice)
        choices.append(choice)
        # turn += 1
        # player = play_turn(turn)
        spots[int(choice)] = player
        sign_victory = check_victory(spots, turn)
        if sign_victory != None and sign_victory != "Draw":
            print(f"Player {sign_victory} won!")
            print(draw_board(spots))
            restart_game()
            break
        elif sign_victory == 'Draw': 
            print(draw_board(spots))
            print("Draw!")
            restart_game()
            break

game_loop()
