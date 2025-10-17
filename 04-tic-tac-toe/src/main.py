#tic tac teo game
import random
class TicTacTeo:
    def __init__(self):
        self.board = [" "] * 10
        self.player_turn = self.get_frist_player()
    def get_frist_player(self):
        return "X" if random.randint(0,1) == 0 else "O"
    def swap_player_turn(self):
        self.player_turn = "X" if self.player_turn == "O" else "O"
    def show_board(self):
        print("\n")
        for i in range(3):
            print(f"{self.board[3*i + 1]} | {self.board[3*i + 2]} | {self.board[3*i + 3]}")
            if i <2:
                print('-' * 9)
        print("\n")
