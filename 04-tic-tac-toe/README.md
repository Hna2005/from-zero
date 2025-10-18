# 03-tic-tac-toe
A Python CLI game where you play classic Tic-Tac-Toe against a computer opponent.
Built with object-oriented programming to practice class design and game logic in Python.
Inspired by beginner-friendly game projects on GitHub.

## Requirements
- Python 3.9+
- No external dependencies required

## Installation
Clone the repository:
```bash
git clone https://github.com/Hna2005/from-zero.git
cd from-zero
```
## Usage
Go inside the `03-tic-tac-toe/` folder and run the game script:
``` bash
python tic_tac_toe.py
```
## Gameplay
- The game randomly selects who starts first: Player (X) or Computer (O).
- The board is displayed as a 3x3 grid numbered 
``` bash
1–9:
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

```
- On your turn, enter a number (1–9) to place your mark.
- The computer makes random valid moves.
- The game ends when:
- A player wins by aligning three marks.
- The board is full (draw).

## Project structure
```graphql
03-tic-tac-toe/
│
├── tic_tac_toe.py         # main game logic and CLI loop
```
## Notes
- The game uses simple AI (random moves) for the computer.
- Input validation ensures players can't choose occupied cells or invalid numbers.
- You can extend the game with smarter AI or a GUI using libraries like Tkinter or Pygame.

## What I learned
This project helped me practice object-oriented programming in a game context:
- Designing a class to manage game state and logic
- Handling user input and turn-based flow
- Implementing win conditions and board rendering





