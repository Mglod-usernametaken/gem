import pygame
from functions_marcel import *
import moviepy.editor


pygame.init()
banner_y_pos = 700
step = 10


#main loop
run = True
while run:
    
    # event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: # to można napisać jako funkcję
            if event.key == pygame.K_LEFT:
                player_rect.left -= step
            if event.key == pygame.K_RIGHT:
                player_rect.right += step
            if event.key == pygame.K_UP:
                player_rect.top -= step
            if event.key == pygame.K_DOWN:
                player_rect.bottom += step
        
        if event.type == pygame.MOUSEMOTION:
           # (player_rect.x, player_rect.y) = event.pos
            player_rect.center = event.pos
    # blit objects
    screen.blit(background,(0,0))
    screen.blit(banner_surf,banner_rect)
    banner_move2()
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(banner_rect):
        print('collision')
        # add delay
#    mouse_pos = pygame.mouse.get_pos()
#    if player_rect.collidepoint(mouse_pos):
#        print('mouse collision')

    # screen refreshing
    pygame.display.update()
    clock.tick(60)

pygame.quit()
