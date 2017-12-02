import pygame

pygame.init() #initializes pygame

gameDisplay = pygame.display.set_mode((800,600)) #creates canvas/ takes tuple

pygame.display.set_caption('Slither') #titles game window

pygame.display.update()
#same as pygame.display.flip() but this acts as flipbook, also this can change less

gameExit = False

while not gameExit:
    for event in pygame.event.get(): 
        #pygame.org/docs/ref/html <- list of all possible events
        if event.type == pygame.QUIT: #checks type of event
            gameExit = True

pygame.quit() #uninitializes
quit() #kills game

