import random


def find_similar(list_of_persons: list[int]) -> bool:
    """
    Checks whether at least two people share the same birthday.

    Args:
        list_of_persons (list[int]): A list of birthdays (numbers between 1 and 365).

    Returns:
        bool: True if there is at least one duplicate birthday, False otherwise.
    """
    return len(list_of_persons) != len(set(list_of_persons))


def probability(group_size: int, num_trials: int) -> float:

    """
    Estimates the probability that at least two people in a group of 57
    share the same birthday (the Birthday Paradox).

    Args:
        n (int): Number of simulation trials.

    Returns:
        float: Estimated probability of at least one shared birthday.
    """
    success_count: int = 0

    for _ in range(num_trials):
        persons: list[int] = [random.randint(1, 365) for _ in range(group_size)]
        if find_similar(persons):
            success_count += 1

    return success_count / num_trials

if __name__ == "__main__":
    NUM_TRIALS = 10_000
    GROUP_SIZE = 23
    
    p = probability(GROUP_SIZE, NUM_TRIALS)
    
    print(f"Simulating for a group of {GROUP_SIZE} people...")
    print(f"The estimated probability of a shared birthday is: {p:.2%}")