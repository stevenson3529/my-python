import pygame

pygame.init()
window = pygame.display.set_mode((500,500))

while True:
    pygame.draw.circle(window, (255,255,0),(250,200),20,2)
    pygame.display.update()
