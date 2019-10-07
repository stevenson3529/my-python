import pygame

pygame.init()
window = pygame.display.set_mode((500,500))

while True:
    pygame.draw.ellipse(window,(255,0,0),(100,100,100,100))
    #pygame.draw.ellipse(window,(0,255,0),(100,150,80,40))
    #pygame.draw.ellipse(window,(0,0,255),(100,190,60,30))
    pygame.draw.circle(window,(0,255,0),(250,250),50,0)
    pygame.display.update()
