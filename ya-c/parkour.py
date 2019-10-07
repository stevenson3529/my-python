'''
Script for a parkour game
'''
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

points = 0
global totalPts 


def easyFinish(points): 
    points = points + 1
    mc.postToChat("You have finished the Easy course. You now have " + str(points) + " points.")

def howMany(points):
    totalPts = totalPts + points
    mc.postToChat("You have " + str(totalPts) + " points in total.")
    
while True:
    pos = mc.player.getTilePos()
    
    if pos.x == 28 and pos.y == 11 and pos.z == 6:
        easyFinish(points)
        time.sleep(5)
        
    if pos.x == 22 and pos.y == 7 and pos.z == 10:
        howMany(points)
        time.sleep(1)





            
