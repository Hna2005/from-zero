import random

class TicTacToe:
    """
    A simple Tic Tac Toe game for CLI.
    
    The board is represented as a list of 10 elements (index 0 is unused).
    Players are 'X' and 'O', and the computer plays as 'O'.
    """

    def __init__(self):
        """Initialize the board and randomly choose the starting player."""
        self.board = [" "] * 10
        self.player_turn = self.get_first_player()

    def get_first_player(self) -> str:
        """Randomly choose the first player ('X' or 'O')."""
        return "X" if random.randint(0, 1) == 0 else "O"
    
    def swap_player_turn(self):
        """Swap the current player."""
        self.player_turn = "X" if self.player_turn == "O" else "O"

    def show_board(self):
        """Print the current state of the board."""
        print("\n")
        for i in range(3):
            print(f"{self.board[3*i + 1]} | {self.board[3*i + 2]} | {self.board[3*i + 3]}")
            if i < 2:
                print("-" * 9)
        print("\n")

    def get_player_move(self, cell: int, player: str) -> bool:
        """
        Place the player's mark on the board if the cell is empty.
        
        Args:
            cell (int): Cell number (1-9)
            player (str): 'X' or 'O'
        
        Returns:
            bool: True if move was successful, False otherwise
        """
        if self.board[cell] == " ":
            self.board[cell] = player
            return True
        return False

    def is_board_full(self) -> bool:
        """Check if the board is full."""
        return " " not in self.board[1:]

    def player_won(self, player: str) -> bool:
        """Check if the given player has won."""
        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def computer_move(self):
        """Let the computer play its move (always as 'O')."""
        empty_blocks = [i for i in range(1, 10) if self.board[i] == " "]
        if empty_blocks:
            choice = random.choice(empty_blocks)
            self.get_player_move(choice, "O")

    def play(self):
        """Start the game loop."""
        print(f"{self.player_turn} starts first!")

        while True:
            self.show_board()

            if self.player_turn == "X":
                try:
                    cell = int(input(f"Player {self.player_turn}, enter your cell (1-9): "))
                    if cell not in range(1, 10) or not self.get_player_move(cell, self.player_turn):
                        print("Invalid move! Try again.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 9.")
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
    game = TicTacToe()
    game.play()
