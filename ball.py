import pygame
import random
import os

WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 600

# Load bounce sound
bounce_sound_path = os.path.join("Assets", "bounce.wav")
bounce_sound = pygame.mixer.Sound(bounce_sound_path)

class Ball:
    # def __init__(self, x, y, radius=10):
    #     self.radius = radius
    #     self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
    #     self.speed_x = random.choice([-5, 5])
    #     self.speed_y = random.choice([-5, 5])

    # def draw(self, surface):
    #     pygame.draw.ellipse(surface, WHITE, self.rect)

    # def move(self):
    #     self.rect.x += self.speed_x
    #     self.rect.y += self.speed_y

    #     if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
    #         self.speed_y *= -1

    # def check_collision(self, paddle1, paddle2):
    #     if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
    #         self.speed_x *= -1

    # def reset(self):
    #     self.rect.center = (WIDTH // 2, HEIGHT // 2)
    #     self.speed_x *= random.choice([-1, 1])
    #     self.speed_y = random.choice([-5, 5])
    
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x = 5
        self.speed_y = 5
        self.radius = 15
        self.color = (255, 255, 255)

        # Load bounce sound
        bounce_sound_path = os.path.join("Assets", "bounce.wav")
        try:
            self.bounce_sound = pygame.mixer.Sound(bounce_sound_path)
        except pygame.error as e:
            print("Error loading sound:", e)
            self.bounce_sound = None

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off edges
        if self.x - self.radius <= 0 or self.x + self.radius >= 800:
            self.speed_x *= -1
            if self.bounce_sound:
                self.bounce_sound.play()
        if self.y - self.radius <= 0 or self.y + self.radius >= 600:
            self.speed_y *= -1
            if self.bounce_sound:
                self.bounce_sound.play()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def reset(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x = 5
        self.speed_y = 5
