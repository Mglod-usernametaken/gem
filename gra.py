import pygame
import sys

# Inicjalizacja pygame
pygame.init()

# Ustawienia okna
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gra")

# Ustawienia bloku
block_size = 50
block_x = 375
block_y = 450
block_speed = 30

# Ustawienia przeszkód
obstacles = [(150, 300, 100, 50), (550, 200, 50, 100), (300, 100, 50, 300)]

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


def draw():
    # Wyczyszczenie ekranu
    window.fill((0, 0, 0))

    # Rysowanie bloku
    pygame.draw.rect(window, (255, 0, 0), (block_x, block_y, block_size, block_size))

    # Rysowanie przeszkód
    for obstacle in obstacles:
        pygame.draw.rect(window, (255, 255, 255), obstacle)

    # Rysowanie zagadki
    if game_state == 1:
        pygame.draw.rect(window, (255, 255, 255), puzzle_input_rect, 2)
        puzzle_input_text = puzzle_font.render(puzzle_answer, True, (255, 255, 255))
        window.blit(puzzle_input_text, (puzzle_input_rect.x + 10, puzzle_input_rect.y + 10))
        window.blit(puzzle_text, puzzle_text_rect)


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
        pygame.time.Clock().tick(60)