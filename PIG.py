# Code based on youtube video https://www.youtube.com/watch?v=NpmFbWO6HPU&t=19s

import random

def roll():
    min_val = 1
    max_val = 6

    return random.randint(min_val, max_val)

while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
        break
    else:
        print("Invalid input. Please enter a number.")


max_score = 50

#Underscore used for placeholders when we don't want to use variable
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    current_score = 0

    should_roll = input("Would you like to role?(y)").lower()
    
    if should_roll != 'y':
        break


    value = roll()
    if value == 1:
        print("You rolled a 1, your turn is over")
    else:
        print("You rolled a ", value)
        


    