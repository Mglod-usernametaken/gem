import pygame
import random

pygame.init()

# Set up the game window
width = 1200
height = 700
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
food_amount = 3

# Set up the snake block size and speed
block_size = 20
clock = pygame.time.Clock()
snake_speed = 30

# Set up the font for the score display
font = pygame.font.SysFont(None, 25)
font2 = pygame.font.SysFont(None, 15)

# Define a function to display the score
def score(score):
    text = font.render("Score: "+str(score), True, black)
    game_display.blit(text, [0, 0])

# Define a function to display the math question on the top of the game window
def math_question(first_num, second_num, operator):
    text = font.render(str(first_num) + " " + operator + " " + str(second_num) + " = ?", True, black)
    game_display.blit(text, [0, 20])

# Define the main game loop
def game_loop():
    game_over = False
    game_close = False

    # Set up the initial position and length of the snake
    x1 = 600
    y1 = 300
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1

    # Set up the initial position of the food
    food_positions = []

    # Set up the math question
    first_num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    operator = random.choice(["+", "-", "*"])
    if operator == "+":
        correct_answer = first_num + second_num
    elif operator == "-":
        correct_answer = first_num - second_num
    else:
        correct_answer = first_num * second_num

    food_positions.append((food_x, food_y, font.render(str(correct_answer), True, black), 'good'))

    for i in range(food_amount):  # generate 2 foods
        food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
        food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
        food_number = random.randrange(correct_answer - 5, correct_answer + 5, 1)
        if food_number == correct_answer:
            food_number = correct_answer + 1
        food_text = font.render(str(food_number), True, black)
        food_positions.append((food_x, food_y, food_text, 'bad'))

    # Main game loop
    while not game_over:
        # If the game is over, display the final score and wait for the user to quit the game
        while game_close == True:
            game_display.fill(white)
            score(length_of_snake - 1)

            message("Przegrałeś! Wciśnij Q aby wyjść lub C aby grać dalej", red)
            pygame.display.update()

            # Wait for user input to either quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # If the snake hits the boundaries of the game window, end the game
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the position of the snake and the length of the snake if it eats the food
        x1 += x1_change
        y1 += y1_change
        game_display.fill(white)

        if not food_positions:
            # Set up the math question
            first_num = random.randint(1, 10)
            second_num = random.randint(1, 10)
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            operator = random.choice(["+", "-", "*"])
            if operator == "+":
                correct_answer = first_num + second_num
            elif operator == "-":
                correct_answer = first_num - second_num
            else:
                correct_answer = first_num * second_num

            # Add the correct answer to the food positions
            food_positions.append((food_x, food_y, font.render(str(correct_answer), True, black), 'good'))

            picked_numbers = [correct_answer]
            for i in range(food_amount):
                food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
                food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
                food_number = random.randrange(correct_answer - 5, correct_answer + 5, 1)
                if food_number in picked_numbers:
                    food_number = correct_answer + 1
                picked_numbers.append(food_number)
                food_text = font.render(str(food_number), True, black)
                food_positions.append((food_x, food_y, food_text, 'bad'))

            picked_numbers.clear()

        # Draw all the food items
        for food in food_positions:
            pygame.draw.rect(game_display, red, [food[0], food[1], block_size, block_size])
            food_text_rect = food[2].get_rect(center=(food[0] + block_size / 2, food[1] + block_size / 2))
            game_display.blit(food[2], food_text_rect)

        # If the snake eats a food item, remove it from the list and increase the length of the snake
        for food in food_positions:
            if x1 == food[0] and y1 == food[1] and food[3] == 'bad':
                game_close = True
                break
            if x1 == food[0] and y1 == food[1]:
                food_positions.clear()
                length_of_snake += 1

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # If the snake hits itself, end the game
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        for x in snake_list:
            pygame.draw.rect(game_display, black, [x[0], x[1], block_size, block_size])

        # Update the score and the display
        score(length_of_snake - 1)
        math_question(first_num, second_num, operator)

        pygame.display.update()

        # Update the clock and the snake speed
        clock.tick(snake_speed)

    # Quit the game and the Pygame library
    pygame.quit()
    quit()

def message(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [width / 2 - 200, height / 2])

# Call the main game loop
game_loop()