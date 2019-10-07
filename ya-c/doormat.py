import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(0.1)
    pos = mc.player.getTilePos()

    if pos.x == -12 and pos.y == 6 and pos.z == 4:
        mc.postToChat("welcome Home")
