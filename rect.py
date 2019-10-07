import pygame

pygame.init()
window = pygame.display.set_mode((500,400))

while True:
    pygame.draw.rect(window,(255,50,175),(0,0,50,50))
    pygame.draw.rect(window,(0,255,0),(100,100,75,54))
    pygame.draw.rect(window,(0,0,255),(200,200,60,80))                     
    pygame.display.update()
    

                
