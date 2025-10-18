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

    def get_player_move(self, cell, player):
        if self.board[cell] == " ":
            self.board[cell] = player
            return True
        else:
            return False

    def is_board_full(self):
        return " " not in self.board[1:]
    
    def player_won(self, player):
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),
                            (1, 5, 9), (3, 5, 7)]
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == player:
                return True
        return False
    
    def computer_move(self):
        empty_blocks = [i for i in range(1, 10) if self.board[i] == " "]
        computer_choice = random.choice(empty_blocks)
        self.get_player_move(computer_choice, self.player_turn)

def game(self):
    print(f"{self.player_turn} starts first!")

    while True:
        self.show_board()

        if self.player_turn == "X":
            try:
                cell = int(input(f"Player {self.player_turn}, enter your cell (1-9): "))
                if cell in range(1, 10) and self.get_player_move(cell, self.player_turn):
                    pass
                else:
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")
                continue
        else:
            print("Computer is thinking...")
            self.computer_move()

        if self.player_won(self.player_turn):
            self.show_board()
            print(f"Player {self.player_turn} wins!")
            break

        if self.is_board_full():
            self.show_board()
            print("It's a draw!")
            break

        self.swap_player_turn()

if __name__ == "__main__":
    # Create a game and start it
    game = TicTacToe()
    game.start()