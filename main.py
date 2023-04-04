import pygame


SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1440

#initial setup
pygame.init()
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The gem')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

#surfaces
screen.fill('#3b3d40')
background = pygame.Surface((1440,800))
background = pygame.image.load('sprites/test.png')

banner = pygame.Surface((900,200))
banner = pygame.image.load('sprites/test-banner.png')
banner_y_pos = 700

text_surface = test_font.render('this text is rendered by pygame', True, 'crimson')

#main loop
run = True
while run:
    
    # event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background,(0,0))
    screen.blit(banner,(270,banner_y_pos))
    banner_y_pos -= 1
    if banner_y_pos <= -200:
        banner_y_pos = 900
    screen.blit(text_surface,(720,300))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
