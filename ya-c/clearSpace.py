import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
sizeToClear = int(input("Please enter how many blocks to clear >"))
mc.setBlocks(pos.x, pos.y, pos.z, pos.x + sizeToClear, pos.y + sizeToClear, pos.z + sizeToClear, block.AIR.id)
