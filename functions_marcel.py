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

banner = pygame.Surface((900,200))
banner = pygame.image.load('sprites/test-banner.png').convert_alpha()
# banner_y_pos = 700

player_surface = pygame.image.load('sprites/character.png').convert_alpha()

# text_surface = test_font.render('this text is rendered by pygame', True, 'crimson')



game_state = 0


def playmovie(video_path):
    movie = moviepy.editor.VideoFileClip(video_path)
    movie.preview()

def banner_move():
    banner_y_pos -=1
    if banner_y_pos <= -200:
        banner_y_pos = 900
