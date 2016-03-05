""" 
by Jez Dean / Public Domain
"""

import microbit from *


while True:
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():   
        microbit.display.show(Image.ANGRY)
    elif microbit.button_a.is_pressed():
        microbit.display.show(Image.HAPPY)
    elif microbit.button_b.is_pressed():
        microbit.display.show(Image.SAD)
    microbit.sleep(100)