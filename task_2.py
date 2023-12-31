
import pygame
import time
import random

pygame.init()

window_width = 720
window_height = 480
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

font = pygame.font.SysFont("times new roman", 40)

snake_speed = 15
speed_level = 1
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
fruit_position = [
    random.randrange(1, (window_width // 10)) * 10,
    random.randrange(1, (window_height // 10)) * 10,
]
fruit_spawn = True
score = 0
high_score = 0


def show_score():
    score_text = font.render("Score : " + str(score), True, white)
    game_window.blit(score_text, [10, 10])


def game_over():
    global high_score
    game_over_text = font.render("Game Over! Score: " + str(score), True, red)
    game_window.blit(game_over_text, [window_width // 4, window_height // 2])

    if score > high_score:
        high_score = score
    high_score_text = font.render("High Score : " + str(high_score), True, white)
    game_window.blit(high_score_text, [window_width // 4, window_height // 1.8])

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and snake_direction != "DOWN":
        snake_direction = "UP"
    if change_to == "DOWN" and snake_direction != "UP":
        snake_direction = "DOWN"
    if change_to == "LEFT" and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    if change_to == "RIGHT" and snake_direction != "LEFT":
        snake_direction = "RIGHT"

    if snake_direction == "UP":
        snake_position[1] -= 10
    if snake_direction == "DOWN":
        snake_position[1] += 10
    if snake_direction == "LEFT":
        snake_position[0] -= 10
    if snake_direction == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if (
        snake_position[0] == fruit_position[0]
        and snake_position[1] == fruit_position[1]
    ):
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_width // 10)) * 10,
            random.randrange(1, (window_height // 10)) * 10,
        ]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(
        game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)
    )

    if (
        snake_position[0] < 0
        or snake_position[0] >= window_width
        or snake_position[1] < 0
        or snake_position[1] >= window_height
    ):
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score()
    pygame.display.update()

    if score >= 50 * speed_level:
        speed_level += 1
        snake_speed += 5

    pygame.time.Clock().tick(snake_speed)
