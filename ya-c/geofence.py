import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

X1 = 19
Z1 = 15
X2 = 24
Z2 = 20

rent = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x > X1 and pos.x < X2 and pos.z > Z1 and pos.z < Z2:
        rent = rent + 0.50
        mc.postToChat("You owe $" + str(rent))
