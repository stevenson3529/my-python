import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

# create live tnt mc.setBlock(pos.x + 2, pos.y, pos.z, block.TNT.id,1)

for x in range(5):
    mc.setBlock(pos.x + 3, pos.y, pos.z + x, block.BEDROCK.id)
    mc.setBlock(pos.x + 3, pos.y + 1, pos.z + x, block.BEDROCK.id)
    mc.setBlock(pos.x + 3, pos.y + 2, pos.z + x, block.BEDROCK.id)
    mc.setBlock(pos.x + 3, pos.y + 3, pos.z + x, block.BEDROCK.id)
    mc.setBlock(pos.x + 3, pos.y + 4, pos.z + x, block.BEDROCK.id)

mc.setBlock(pos.x + 3, pos.y + 1, pos.z + 1, block.SAND.id)
mc.setBlock(pos.x + 3, pos.y + 1, pos.z + 3, block.SAND.id)
mc.setBlock(pos.x + 3, pos.y + 3, pos.z + 1, block.SAND.id)
mc.setBlock(pos.x + 3, pos.y + 3, pos.z + 3, block.SAND.id)
mc.setBlock(pos.x + 3, pos.y + 2, pos.z + 2, block.SAND.id)


