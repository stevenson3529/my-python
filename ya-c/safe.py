import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def safeFeet():
    pos = mc.player.getTilePos()
    #getBlock() gets th id of the block at
    #the co-ordinates you provide
    b = mc.getBlock(pos.x, pos.y -1, pos.z)
    #check if player is on air or water
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block == WATER_FLOWING.id:
        mc.postToChat('not safe')
    else:
        mc.postToChat('safe')

while True:
    #time.sleep(0.5)
    safeFeet()
