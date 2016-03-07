"""
    8-Ball Message Generator

    Copyright (c) 2016 Multiple Authors

    MIT  Licence

"""

from microbit import *
import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it"
    "My reply is no",
    "My sources say no",
    "Outlook not so good"
    "Very doubtful"
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
