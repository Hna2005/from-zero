# 03-Simulation
**Classic Probability Simulations:**

This repository contains Python simulations for classic probability problems to verify theoretical outcomes through computation.

- **Monty Hall Problem**
- **Birthday Problem**

## Requirements
- Python 3.8+

## Project Structure
```graphql
03-simulation/
│
├── src/
│   ├── monty_hall.py       # Simulates the Monty Hall problem
│   └── birthday_problem.py # Simulates the Birthday Paradox
│
└── README.md               # Project documentation
```
## Installation
Make sure you have Python 3.8+ installed. Clone the repository:
```bash
git clone https://github.com/Hna2005/from-zero.git
cd from-zero
```
## Usage
**1. Monty Hall Problem**

This script simulates the Monty Hall problem to show that switching doors increases the probability of winning from `~33%` to `~66%`.
Open your terminal and run the following command:
```bash
python monty_hall.py
```
Expected Output:
```bash
Running 100,000 simulations...
Wins without switching: 33245 (33.25%)
Wins with switching:    66755 (66.76%)
```
**2. birthday problem**
This script calculates the surprisingly high probability that at least two people in a group share a birthday.
Open your terminal and run the following command:
```bash
python birthday_problem.py
```
Expected Output:
```bash
Simulating for a group of 23 people...
The estimated probability of a shared birthday is: 50.45%
```

## Postmortem: Bug in Monty Hall Simulation

### Problem Description
This project simulates the classic Monty Hall problem (3 doors: one car, two goats).  
Two strategies are compared:
- Not switching (stick with the initial choice)
- Switching (change to the remaining unopened door)

In probability theory, the expected outcomes are:
- Not switching → ~33% win rate
- Switching → ~66% win rate

However, in the initial implementation both strategies produced almost identical results, which was incorrect.
### Root Cause
In the first version of the switch function, the host always opened the first available goat door:

```python
open_door = [i for i in range(3) if i != first_choice and rooms[i] != 'car'][0]
```
### Fix

The door opened by the host must be chosen randomly:

```python 
open_door = random.choice(
    [i for i in range(3) if i != first_choice and rooms[i] != 'car']
)
```

Results (`100,000` trials)

not_switch(`100000`) → ~`33,000` wins

switch(`100000`) → ~`66,000` wins

The simulation now matches the theoretical probabilities.

## Key Takeaways

- Always check for hidden biases in deterministic choices (e.g., using [0] in a list).

- Randomization matters when simulating probabilistic scenarios.

- Unit tests or sanity checks against expected probabilities can help catch such issues early.
