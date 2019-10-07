import pygame

pygame.init()
window = pygame.display.set_mode((500,400))

while True:
    pygame.draw.line(window,(255,255,0),(50,50),(75,75),3)
    pygame.draw.line(window,(255,255,0),(75,75),(25,75),3)
    pygame.draw.line(window,(255,255,0),(25,75),(50,50),3)
    pygame.display.update()
