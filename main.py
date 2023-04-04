import pygame


SCREEN_HEIGHT = 1200
SCREEN_WIDTH = 1600

screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pley the gem')

run = True
while run:
    
    # event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
