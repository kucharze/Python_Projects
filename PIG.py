# Code based on youtube video https://www.youtube.com/watch?v=NpmFbWO6HPU&t=19s

import random
from gtts import gTTS
import os
import time
import sys
import pyautogui

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

