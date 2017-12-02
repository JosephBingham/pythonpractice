import pygame, sys
from pygame.locals import *

pygame.init() #initialize game
DISPLAYSURF = pygame.display.set_mode((400, 300)) #sets display
pygame.display.set_caption('Hello World!') #sets caption
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
