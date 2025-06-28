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

    for player_idx in range(players):
        print("Player", player_idx + 1, "turn")
        print("Your total score is", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to role?(y)").lower()
            
            if should_roll != 'y':
                break


            value = roll()
            if value == 1:
                print("You rolled a 1, your turn is over")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a ", value)
                

            print("Your current score is", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is", player_scores[player_idx])



max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "wins with a score of", max_score)