#!/usr/bin/python
import pygame, sys
from pygame.locals import *

pygame.init() #initialize game
DISPLAYSURF = pygame.display.set_mode((700, 600)) #sets display
pygame.display.set_caption('Hangman') #sets caption

#pygame.draw.circle(DISPLAYSURF, (300, 50), 20, 0)

while True: #main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()














