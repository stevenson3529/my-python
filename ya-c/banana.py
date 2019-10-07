import microbit
import time

IMG = microbit.Image('00900:00990:00090:00900:09000')

while True:
    time.sleep(0.2)
    if microbit.pin0.is_touched():
        microbit.display.show(IMG)
    else:
        microbit.display.show(microbit.Image.SAD)
        
