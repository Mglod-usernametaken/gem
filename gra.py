import pygame
import sys
from gra_functions import *
# import moviepy.editor

# Inicjalizacja pygame
pygame.init()
clock = pygame.time.Clock()

# surfaces
window.fill(('#3b3d40'))
background = pygame.Surface((1440,800))
background = pygame.image.load('sprites/test.png')

# Ustawienia zagadki
puzzle_answer = ""
puzzle_font = pygame.font.SysFont("Arial", 40)
puzzle_text = puzzle_font.render("Podaj odpowiedź:", True, (255, 255, 255))
puzzle_text_rect = puzzle_text.get_rect()
puzzle_text_rect.center = (window_width // 2, window_height // 2 - 50)
puzzle_input_rect = pygame.Rect(window_width // 2 - 100, window_height // 2 + 25, 200, 50)
puzzle_active = False

# Stan gry
game_state = 0


# Główna pętla gry
while True:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game_state == 0:
                # Poruszanie blokiem
                if event.key == pygame.K_LEFT:
                    block_x -= block_speed
                elif event.key == pygame.K_RIGHT:
                    block_x += block_speed
                elif event.key == pygame.K_UP:
                    block_y -= block_speed
                elif event.key == pygame.K_DOWN:
                    block_y += block_speed

                # Collision detection
                block_rect = pygame.Rect(block_x, block_y, block_size, block_size)
                for obstacle in obstacles:
                    obstacle_rect = pygame.Rect(obstacle)
                    if block_rect.colliderect(obstacle_rect):
                        print("Kolizja!")
                        playmovie('sound/test.mp4')

            elif game_state == 1:
                # Wprowadzanie odpowiedzi
                if event.type == pygame.KEYDOWN:
                    if puzzle_active:
                        if event.key == pygame.K_RETURN:
                            if puzzle_answer == "Python":
                                game_state = 2
                            else:
                                puzzle_answer = ""
                        elif event.key == pygame.K_BACKSPACE:
                            puzzle_answer = puzzle_answer[:-1]
                        else:
                            puzzle_answer += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game_state == 1:
                        # Aktywacja pola do wprowadzania odpowiedzi
                        if puzzle_input_rect.collidepoint(event.pos):
                            puzzle_active = True
                        else:
                            puzzle_active = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if game_state == 1:
                        puzzle_active = False

        # Rysowanie elementów na ekranie
        draw()

        # Zmiana sceny
        if block_y < 50 and game_state == 0:
            game_state = 1
            block_y = 550

        # Odświeżenie ekranu
        pygame.display.update()
        clock.tick(60)
