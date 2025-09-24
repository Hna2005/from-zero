import random

# The set of the doors
rooms = ["goat", "car", "goat"]


def not_switch(n: int) -> int:
    """
    Simulation Monty Hall problem without switching

    Args:
        n (int): Number of simulation trials.

    Returns:
        int: Number of wins (choosing the car) when the player does not switch.
    """
    wins: int = 0
    for _ in range(n):
        first_choice: int = random.choice(range(3))
        if rooms[first_choice] == "car":
            wins += 1
    return wins


def switch(n: int) -> int:
    """
    Simulates the Monty Hall problem with switching.

    Args:
        n (int): Number of simulation trials.

    Return:
        int: Number of wins (choosing the car) when the player switches doors.
    """
    wins: int = 0
    for _ in range(n):
        first_choice = random.choice(range(3))
        # Host opens a goat door that is not the player's first choice
        open_door = random.choice([i for i in range(3) if i != first_choice and rooms[i] != "car"])
        # Player switches to the only remaining closed door
        switch_choice = [i for i in range(3) if i != first_choice and i != open_door][0]
        if rooms[switch_choice] == "car":
            wins += 1
    return wins

if __name__ == "__main__":
    NUM_TRIALS = 100_000
    
    stay_wins = not_switch(NUM_TRIALS)
    switch_wins = switch(NUM_TRIALS)
    
    print(f"Running {NUM_TRIALS:,} simulations...")
    print(f"Wins without switching: {stay_wins} ({(stay_wins/NUM_TRIALS):.2%})")
    print(f"Wins with switching:    {switch_wins} ({(switch_wins/NUM_TRIALS):.2%})")
