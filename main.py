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
        if game_state ==0:
            if event.type == pygame.KEYDOWN: # to można napisać jako funkcję
                if event.key == pygame.K_LEFT:
                    player_rect.left -= step
                if event.key == pygame.K_RIGHT:
                    player_rect.right += step
                if event.key == pygame.K_UP:
                    player_rect.top -= step
                if event.key == pygame.K_DOWN:
                    player_rect.bottom += step
        if game_state ==1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode

#        if event.type == pygame.MOUSEMOTION:
#           # (player_rect.x, player_rect.y) = event.pos
#            player_rect.center = event.pos

    if game_state ==0:
        # blit objects
        screen.blit(background,(0,0))
        screen.blit(banner_surf,banner_rect)
        banner_move2()
        screen.blit(player_surf,player_rect)

        if player_rect.colliderect(banner_rect):
            print('collision')
            game_state = 1
            # add delay

    elif game_state ==1:
        screen.blit(background2,(0,0))
        text_surf = base_font.render(user_text,True,(255,0,0))
        screen.blit(text_surf,text_rect)
        if user_text == '123':
            user_text = 'enter text'
            player_rect.center = (100,100)
            game_state = 0

#    mouse_pos = pygame.mouse.get_pos()
#    if player_rect.collidepoint(mouse_pos):
#        print('mouse collision')

    # screen refreshing
    pygame.display.update()
    clock.tick(60)

pygame.quit()
