import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
clock = pygame.time.Clock()

windowWidth = 1200
windowHeight = 600

surface = pygame.display.set_mode((windowWidth,windowHeight))

pygame.display.set_caption('keyboard')

mousePosition = None
mousePressed = False

squareSize = 40
squareColour = (192,16,120)
squareX = windowWidth / 2
squareY = windowHeight - squareSize
draggingSquare = False
gravity = 5.0

def checkBounds():
    global squareColour, squareX, squareY, draggingSquare

    if mousePressed == True:
        if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:
            if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:
                draggingSquare = True
                pygame.mouse.set_visible(0)

    else:
        squareColour = (192,16,120)
        pygame.mouse.set_visible(1)
        draggingSquare = False

def checkGravity():

    global gravity, squareY, squareSize,squareHeight

    if squareY < windowHeight - squareSize and mousePressed == False:
        squareY += gravity
        gravity = gravity * 1.1

    else:
        squareY = windowHeight - squareSize
        gravity = 5.0

def drawSquare():
    global squareColour, squareX, squareY, dragggingSquare

    if draggingSquare == True:

        squareColour = (150,210,147)
        squareX = mousePosition[0] - squareSize /2
        squareY = mousePosition[1] - squareSize / 2

    pygame.draw.rect(surface, squareColour, (squareX, squareY, squareSize, squareSize))

def quit():
    pygame.quit()
    sys.exit()

while True:

    mousePosition = pygame.mouse.get_pos()

    surface.fill((28,200,195))

    if pygame.mouse.get_pressed()[0] == True:
        mousePressed = True
    else:
        mousePressed = False

    checkBounds()
    checkGravity()
    drawSquare()

    clock.tick(60)
    pygame.display.update()

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

    
