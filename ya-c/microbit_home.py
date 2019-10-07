import mcpi.minecraft as minecraft
import time
import microbit
mc = minecraft.Minecraft.create()

while True:
    time.sleep(0.1)
    pos = mc.player.getTilePos()

    if pos.x == 72 and pos.y == 3 and pos.z == 107:
        microbit.display.show(microbit.Image.HOUSE)
    else:
        microbit.display.show('?')
