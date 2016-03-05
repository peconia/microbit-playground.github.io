""" 
    8-Ball Message Generator
    
    Copyright (c) 2016 Multiple Authors
    
    MIT  Licence
    
    ************ DOUBLE CHECK THIS WORKS *********************
    
"""

import microbit from *
import random

# an array of strings called MESSAGES
MESSAGES = ["It is certain",
            "Dont count on it",
            "Ask again",
            "Perhaps",
            "Do not bet on it,"
           ]

microbit.display.print("8")     # initialise the display
while True:
    if microbit.accelerometer.is_gesture('shake') is True:
            microbit.display.scroll(random.choice(MESSAGES))   # message to show picked at random
            microbit.sleep(2000)                         # Show the message for 2 Seconds
            microbit.display.print("8")
    sleep(100)      #slow down the while loop