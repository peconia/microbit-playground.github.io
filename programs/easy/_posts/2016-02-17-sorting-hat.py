"""
    Harry Potter Sorting Hat

    Copyright (c) 2016 Jez Dean

    MIT  Licence

"""
# import microbit and random modules
import microbit from *
import random

# create array of strings called HOUSES
HOUSES   = ["Gryffindor",
            "Slytherin",
            "Ravenclaw",
            "Hufflepuff",
           ]

# create an endless loop waiting for button_a to be pressed
while True:
    if microbit.button_a.is_pressed():
        microbit.display.scroll(random.choice(HOUSES))
    microbit.sleep(100)
