import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
clock = pygame.time.Clock()

windowWidth = 640
windowHeight = 480

surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('shaaapes')

squareX = 0
squareY = 0

greenSquareX = windowWidth/2
greenSquareY = windowHeight/2

blueSquareX = 0.0
blueSquareY = 0.0
blueSquareVX = 1
blueSquareVY = 1

while True:
    #surface.fill((255,255,0))
    pygame.draw.rect(surface,(255,0,0),(random.randint(0,windowWidth),random.randint(0,windowHeight),10,10))

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.update()
