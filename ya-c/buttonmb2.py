import microbit
import time
print('press a')

while True:
    if microbit.button_a.was_pressed():
        print('a pressed')
        microbit.display.show('A')
        time.sleep(0.5)
        microbit.display.clear()
