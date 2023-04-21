import pygame
import sys

window_width = 1440
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

block_size = 32
block_x = 375
block_y = 450
block_speed = 32

obstacles = [(150, 300, 100, 50), (550, 200, 50, 100), (300, 100, 50, 300)]

character = pygame.draw.rect(window, (255, 0, 0), (block_x, block_y, block_size, block_size))
game_state = 0

def draw():
     # Wyczyszczenie ekranu
     window.fill(('#3b3d40'))
     window.blit(character)
     
     # Rysowanie przeszkód
     for obstacle in obstacles:
         pygame.draw.rect(window, (255, 255, 255), obstacle)

     # Rysowanie zagadki
     if game_state == 1:
         pygame.draw.rect(window, (255, 255, 255), puzzle_input_rect, 2)
         puzzle_input_text = puzzle_font.render(puzzle_answer, True, (255, 255, 255))
         window.blit(puzzle_input_text, (puzzle_input_rect.x + 10, puzzle_input_rect.y + 10    ))
         window.blit(puzzle_text, puzzle_text_rect)

def playmovie(video_path):
    movie = pygame.movie.Movie(video_path)
    mrect = pygame.Rect(0,0,1440,800)
    movie.set_display(screen,mrect.move(65,150))
    movie.set_volume(10)
    movie.play()
