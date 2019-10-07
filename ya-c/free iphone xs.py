import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()

    if pos.x == -9 and pos.y == 14 and pos.z == -13:
        mc.postToChat("You just won a FREE iPhone Xs!*")
        mc.postToChat("*this message is 100% not fake... :)")
