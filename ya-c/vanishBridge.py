import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
bridge = []

def buildBridge():
    pos = mc.player.getTilePos()
    #getBlock() gets th id of the block at
    #the co-ordinates you provide
    b = mc.getBlock(pos.x, pos.y -1, pos.z)
    #check if player is on air or water
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block == WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y -1, pos.z, block.GLOWING_OBSIDIAN.id)
        coordinate = [pos.x, pos.y - 1, pos.z]
        bridge.append(coordinate)
    elif b != block.GLOWING_OBSIDIAN.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0],
            coordinate[1],coordinate[2],block.AIR.id)
            time.sleep(0.25)

while True:
    time.sleep(0.2)
    buildBridge()
