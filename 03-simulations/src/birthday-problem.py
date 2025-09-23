import random

rooms = ["goat", "car", "goat"]


def not_switch(n):
    wins = 0
    for _ in range(n):
        first_choice = random.choice(range(3))
        if rooms[first_choice] == "car":
            wins += 1
    return wins


def switch(n):
    wins = 0
    for _ in range(n):
        first_choice = random.choice(range(3))
        open_door = random.choice([i for i in range(3) if i != first_choice and rooms[i] != "car"])
        switch_choice = [i for i in range(3) if i != first_choice and i != open_door][0]
        if rooms[switch_choice] == "car":
            wins += 1
    return wins
