import os
import pygame
import sys
from ball import Ball

pygame.mixer.init()
# Redirect stdout to suppress the pygame welcome message
sys.stdout = open(os.devnull, 'w')

def custom_init():
    # Replace this with your custom message
    print("Welcome to the custom pygame game!")

    # Initialize pygame
    pygame.init()

# Use the custom init function
custom_init()

from paddle import Paddle


# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping-Pong Game')

# Colors & font
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
font = pygame.font.SysFont('Arial', 40)

# Game states
START_MENU = 0
GAME_PLAY = 1
PAUSE_MENU = 2
game_state = START_MENU

clock = pygame.time.Clock()
running = True

# Create ball
ball = Ball(WIDTH, HEIGHT)

def draw_start_menu():
    screen.fill(BLUE)
    title = font.render("Ping-Pong Game", True, WHITE)
    start = font.render("Press ENTER to Start", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

def draw_pause_menu():
    screen.fill(BLUE)
    paused = font.render("Paused", True, WHITE)
    resume = font.render("Press R to Resume", True, WHITE)
    restart = font.render("Press ENTER to Restart", True, WHITE)
    quit_txt = font.render("Press Q to Quit", True, WHITE)
    screen.blit(paused, (WIDTH // 2 - paused.get_width() // 2, HEIGHT // 3))
    screen.blit(resume, (WIDTH // 2 - resume.get_width() // 2, HEIGHT // 2 - 40))
    screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2))
    screen.blit(quit_txt, (WIDTH // 2 - quit_txt.get_width() // 2, HEIGHT // 2 + 40))
    pygame.display.update()

def draw_game():
    screen.fill((0, 0, 0))
    ball.update()
    ball.draw(screen)
    pygame.display.update()

def handle_game_events():
    global game_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_p]:
                game_state = PAUSE_MENU

def handle_start_menu():
    global game_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game_state = GAME_PLAY

def handle_pause_menu():
    global game_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_state = GAME_PLAY
            elif event.key == pygame.K_RETURN:
                ball.reset(WIDTH, HEIGHT)
                game_state = GAME_PLAY
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

def main():
    global game_state
    while running:
        if game_state == START_MENU:
            draw_start_menu()
            handle_start_menu()
        elif game_state == GAME_PLAY:
            draw_game()
            handle_game_events()
        elif game_state == PAUSE_MENU:
            draw_pause_menu()
            handle_pause_menu()
        clock.tick(60)

if __name__ == '__main__':
    main()