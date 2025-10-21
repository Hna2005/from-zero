# 03-Simulation
**Classic Probability Simulations:**

Classic Probability Simulations with Streamlit Dashboard

This repository contains Python simulations for classic probability problems to verify theoretical outcomes through computation.
It also includes an interactive Streamlit dashboard for visual simulations.

Included Simulations:
- **Monty Hall Problem**
- **Birthday Problem**

## Requirements
- Python 3.8+
Streamlit `(pip install streamlit)`
## Project Structure
```graphql
03-simulation/
│
├── src/
│   ├── main-dashboard.py   # Streamlit dashboard for interactive simulations
│   ├── monty_hall.py       # Simulates the Monty Hall problem
│   └── birthday_problem.py # Simulates the Birthday Paradox
│
└── README.md               # Project documentation

```
## Installation
1. Make sure you have Python 3.8+ installed. 
2. Clone the repository:
```bash
git clone https://github.com/Hna2005/from-zero.git
cd from-zero
```
## Usage
**1. Run Streamlit Dashboard**

Run the interactive dashboard:
```bash
streamlit run src/main-dashboard.py

```
Then open the provided URL in your browser (usually `http://localhost:8501`).

**Birthday Problem:**
Adjust the number of trials and group size to see the estimated probability of shared birthdays.

**Monty Hall Problem:**
Choose the number of simulations and whether to switch doors, then view the probability of winning.

2. Run Individual Scripts (CLI)
Monty Hall Problem:
```bash
python src/monty_hall.py
```
Expected Output:
```bash
Running 100,000 simulations...
Wins without switching: 33,245 (33.25%)
Wins with switching:    66,755 (66.76%)

```
Birthday Problem:
```bash 
python src/birthday_problem.py
```
Expected Output:
```bash
Simulating for a group of 23 people...
Estimated probability of a shared birthday: 50.45%
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
