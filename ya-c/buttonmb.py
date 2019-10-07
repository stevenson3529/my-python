import microbit
import time
print('press a')

while True:
    if microbit.button_a.was_pressed():
        print('a pressed')
        time.sleep(0.05)
