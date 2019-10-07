import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
SIZE = 20

def BuildHouse():

    midx = x + SIZE/2
    midy = y + SIZE/2

    #shell
    mc.setBlocks(x,y,z,x+SIZE, y + SIZE, z + SIZE,block.MELON.id)
    #hollow
    mc.setBlocks(x+1,y,z+1, x + SIZE -1, y +SIZE - 1,z + SIZE - 1,block.AIR.id)
    #door
    mc.setBlocks(midx - 1, y, z, midx +1, y + 3, z, block.AIR.id)
    #window
    mc.setBlocks(x+3, y + SIZE - 3, z , midx - 3, midy + 3, z,block.GLASS.id)
    #window2
    mc.setBlocks(midx+3, y + SIZE - 3,z, x + SIZE -3,midy + 3, z, block.GLASS.id)
    #roof
    mc.setBlocks(x, y + SIZE +1, z, x + SIZE, y + SIZE,z + SIZE,block.GLOWING_OBSIDIAN.id)
    #carpet/floor
    mc.setBlocks(x + 1, y-1, z + 1, x + SIZE - 1, y-1, z + SIZE - 1,block.WOOL.id,8)

pos = mc.player.getTilePos()

x = pos.x +2
y = pos.y
z = pos.z


for h in range(4):
    BuildHouse()
    x = x + SIZE + 3

