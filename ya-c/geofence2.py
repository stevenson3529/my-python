import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

X1 = 14
Z1 = 27
X2 = 19
Z2 = 30

HOME_X = X2 + 2
HOME_Y = 15
HOME_Z = Z2 + 2
rent = 0
inField = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x > X1 and pos.x < X2 and pos.z > Z1 and pos.z < Z2:
        rent = rent + 0.50
        mc.postToChat("You owe m" + str(rent))
        inField = inField + 1
    else: #not in field
        inField = 0
    if inField > 3:
        mc.postToChat("TOO SLOW!!!!!!")
        mc.player.setPos(HOME_X, pos.y + HOME_Y, HOME_Z)
    
