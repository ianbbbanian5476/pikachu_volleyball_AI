import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Test')

WHITE = (255,255,255)
RED = (255,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(400,300),50)
    pygame.display.flip()