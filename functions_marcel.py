import pygame
import sys
import moviepy.editor


SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1440

screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The gem')
clock = pygame.time.Clock()
# test_font = pygame.font.Font(None, 50)

#surfaces
screen.fill('#3b3d40')
background = pygame.Surface((1440,800))
background = pygame.image.load('sprites/test.png').convert()

background2 = pygame.Surface((1440,800))
background2 = pygame.image.load('sprites/test2.png').convert()

banner_surf = pygame.image.load('sprites/test-banner.png').convert_alpha()
banner_rect = banner_surf.get_rect(topleft = (270,700))

player_surf = pygame.image.load('sprites/character.png').convert_alpha()
player_rect = player_surf.get_rect(topleft= (270,200))

base_font = pygame.font.Font(None,64)
user_text = 'enter text'
text_surf = base_font.render(user_text,True,(255,0,255))
text_rect = text_surf.get_rect(center = (720,750))
game_state = 0

step = 16


def playmovie(video_path):
    movie = moviepy.editor.VideoFileClip(video_path)
    movie.preview()

def banner_move2():
    banner_rect.top -=1
    if banner_rect.top <= -200:
        banner_rect.top = 900

def move_with_arrows (event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT :
            player_rect.left -= step
        if event.key == pygame.K_RIGHT :
            player_rect.right += step
        if event.key == pygame.K_UP :
            player_rect.top -= step
        if event.key == pygame.K_DOWN :
            player_rect.bottom += step

