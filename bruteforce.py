import time
from itertools import product
from pynput.keyboard import Key, Controller

chars = '' #enter possible characters in password, need to specify caps

keyboard = Controller()
time.sleep(5) #gives 5 seconds to tab into text box

for length in range(6, 15):
    to_attempt = product(chars, repeat=length)
    for attempt in to_attempt:
        keyboard.type(''.join(attempt))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.01) #waits for windos to respond to the keyboard input, can be modifed