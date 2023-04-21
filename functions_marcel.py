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

banner_surf = pygame.image.load('sprites/test-banner.png').convert_alpha()
banner_rect = banner_surf.get_rect(topleft = (270,700))

player_surf = pygame.image.load('sprites/character.png').convert_alpha()
player_rect = player_surf.get_rect(topleft= (270,200))



game_state = 0


def playmovie(video_path):
    movie = moviepy.editor.VideoFileClip(video_path)
    movie.preview()

def banner_move2():
    banner_rect.top -=1
    if banner_rect.top <= -200:
        banner_rect.top = 900

