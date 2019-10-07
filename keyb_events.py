import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
clock = pygame.time.Clock()
windowHeight = 600
windowWidth = 1000

surface = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('keyybooarrrd')

#square
playerSz = 20
playerX = (windowWidth/2)-(playerSz/2)
playerY = windowHeight - playerSz
playerVX = 1.0
playerVY = 1.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

#keyboard
leftDown = False
rightDown = False
haveJumped = False

def move():
    global playerX,playerY,playerVX,playerVY,haveJumped,gravity

    if leftDown:
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX
        if playerX > 0:
            playerX += playerVX

    if rightDown:
        if playerVX < 0.0:
            playerVX = moveSpeed
        if playerX + playerSz < windowWidth:
            playerX += playerVX

    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else:
        playerVY = 0.0
        havejumped = False

    if playerY < windowHeight - playerSz:
        playerY += gravity
        gravity = gravity * 1.1
    else:
        playerY = windowHeight - playerSz
        gravity = 1.0

    playerY -= playerVY

    if playerVX > 0.0 and playerVX < maxSpeed or playerVX <0.0 and playerVX> -maxSpeed:
        if haveJumped == False:
            playerVX = playerVX *1.1

def quitGame():
    pygame.quit()
    sys.exit()

while True:
    surface.fill((0,0,0))

    pygame.draw.rect(surface, (255,0,0),(playerX,playerY,playerSz,playerSz))

    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped:
                    haveJumped = True
                    playerVY += jumpHeight
            if event.key == pygame.K_ESCAPE:
                quitGame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

    move()

    clock.tick(60)
    pygame.display.update()
                
        
                    
            
                     
