import os
import re

class TicTacToe:
    def __init__(self):
        self.spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        self.choices = []
        self.playerX = 0
        self.playerO = 0
        self.turn = 0
    
    def restart_game(self):
        play_again = input("Would you play again yes or no? ")
        global spots
        if play_again.lower() == "yes":
            self.spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
            self.choices.clear()
            self.turn = 0
            game_loop()
        elif play_again.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.restart_game()

    def check_victory(self):

        winning_combination = [
        (1,2,3), (4,5,6), (7,8,9), 
        (1,4,7), (2,5,8), (3,6,9), 
        (1,5,9), (3,5,7)]

        for combo in winning_combination:
            if self.spots[combo[0]] == self.spots[combo[1]] == self.spots[combo[2]]:
                return self.spots[combo[0]]

        if self.turn == 9:
            return "Draw"

        return None
    
    def check_input(self, choice):
        while True:
            if choice.lower() == 'q':
                print("Thanks for playing!")
                exit()  # Exit the program

            if choice in self.choices:
                print("Number allready choosen, choose another number")
                choice = input("Please choose a number between 1 and 9 or 'q' to quit the game: ")
                continue

            if not re.match("^[1-9]$", choice):
                choice = input("Please choose a number between 1 and 9 or 'q' to quit the game: ")
                continue

            return choice

    def play_turn(self):
        return "O" if self.turn % 2 == 0 else "X"

    def draw_board(self):
        board = f"|{self.spots[1]}|{self.spots[2]}|{self.spots[3]}|\n|{self.spots[4]}|{self.spots[5]}|{self.spots[6]}|\n|{self.spots[7]}|{self.spots[8]}|{self.spots[9]}|\n"
        return board

    def game_loop(self):
        while True:
            print(self.draw_board())
            print(f"Score Player X: { self.playerX}")
            print(f"Score Player O: { self.playerO}")

            self.turn += 1
            player = self.play_turn()

            choice = input(f"Player {player}, choose number between 1 and 9 or q to quit the game: ")
            choice = self.check_input(choice)

            if choice is None:
                break

            self.choices.append(choice)
            # turn += 1
            # player = play_turn(turn)
            self.spots[int(choice)] = player

            sign_victory = self.check_victory()

            if sign_victory is not None and sign_victory != "Draw":
                print(f"Player {sign_victory} won!")
                print(self.draw_board())

                if sign_victory == "X":
                    self.playerX += 1
                if sign_victory == "O":
                    self.playerO += 1

                print(f"Score Player X: {self.playerX}")
                print(f"Score Player 0: {self.playerO}")

                if not self.restart_game():
                    break

            elif sign_victory == 'Draw': 
                print(self.draw_board())
                print("Draw!")
                self.playerO += 1
                self.playerX += 1

                print(f"Score Player X: {self.playerX}")
                print(f"Score Player 0: {self.playerO}")

                if not self.restart_game():
                    break

def main():
    game = TicTacToe()
    game.game_loop()

if __name__ == "__main__":
    main()

# playerX = 0
# playerO = 0

# spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
# choices = []

# def restart_game():
#     play_again = input("Would you play again yes or no? ")
#     global spots
#     if play_again.lower() == "yes":
#         spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
#         choices.clear()
#         game_loop()
#     elif play_again.lower() == "no":
#         print("Thanks for playing!")
#         exit()
#     else:
#         print("Invalid input. Please enter 'yes' or 'no'.")
#         restart_game()

# def check_victory(spots, turn):
#     winning_combination = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(1,5,7)]

#     for combo in winning_combination:
#         if spots[combo[0]] == spots[combo[1]] == spots[combo[2]]:
#             return spots[combo[0]]

#     if turn == 9:
#         return "Draw"
        
#     return None


# def check_input(choice):
#     while True:
#         if choice.lower() == 'q':
#             print("Thanks for playing!")
#             exit()  # Exit the program

#         if choice in choices:
#             print("Number allready choosen, choose another number")
#             choice = input("Please choose a number between 1 and 9 or 'q' to quit the game: ")
#             continue

#         if not re.match("^[1-9]$", choice):
#             choice = input("Please choose a number between 1 and 9 or 'q' to quit the game: ")
#             continue

#         return choice

# def play_turn(number):
#     if number % 2 == 0:
#         return "O"
#     else:
#         return "X"

# def draw_board(spots):
#     board = f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|\n"
#     return board

# def game_loop():
#     turn = 0
#     global playerX
#     global playerO
#     while True:
#         print(draw_board(spots))
#         print(f"Score Player X: { playerX}")
#         print(f"Score Player O: { playerO}")
#         turn += 1
#         player = play_turn(turn)
#         choice = input(f"Player {player}, choose number between 1 and 9 or q to quit the game: ")
#         choice = check_input(choice)
#         choices.append(choice)
#         # turn += 1
#         # player = play_turn(turn)
#         spots[int(choice)] = player
#         sign_victory = check_victory(spots, turn)
#         if sign_victory != None and sign_victory != "Draw":
#             print(f"Player {sign_victory} won!")
#             print(draw_board(spots))
#             if sign_victory == "X":
#                 playerX += 1
#             if sign_victory == "O":
#                 playerO += 1
#             print(f"Score Player X: {playerX}")
#             print(f"Score Player 0: {playerO}")
#             restart_game()
#             break
#         elif sign_victory == 'Draw': 
#             print(draw_board(spots))
#             print("Draw!")
#             playerO += 1
#             playerX += 1
#             print(f"Score Player X: {playerX}")
#             print(f"Score Player 0: {playerO}")
#             restart_game()
#             break

# game_loop()