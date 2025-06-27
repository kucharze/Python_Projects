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
