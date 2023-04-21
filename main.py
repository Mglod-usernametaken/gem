import pygame
from functions_marcel import *
import moviepy.editor


pygame.init()

#main loop
run = True
while run:
    
    # event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            playmovie('sound/test.mp4')

    screen.blit(background,(0,0))
    screen.blit(banner,(270,banner_y_pos))
    banner_y_pos -= 1
    if banner_y_pos <= -200:
        banner_y_pos = 900

    pygame.display.update()
    clock.tick(60)

pygame.quit()
