import random

rooms = ['goast', 'car', 'goast']


def not_sweich(n):
    count = 0
    number_of_true = 0
    
    while count < n:
        frist_choice = random.choice(range(3))
        
        if rooms[frist_choice] == 'car':
            number_of_true += 1
        count += 1
    
    return number_of_true


def sweich(n):
    count = 0
    number_of_true = 0
    
    while count < n:
        frist_choice = random.choice(range(3))
        open_door = [i for i in range(3) if i != frist_choice and rooms[i] != 'car' ][0]
        sewich_choice = [i for i in range(3) if i != frist_choice and i != open_door][0]
        if rooms[sewich_choice] == 'car':
            number_of_true += 1
        count += 1
    
    return number_of_true
