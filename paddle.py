import pygame

WHITE = (255, 255, 255)
HEIGHT = 600

class Paddle:
    def __init__(self, x, y, width=10, height=120, speed=6):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
            if self.rect.top < 0:
                self.rect.top = 0
        else:
            self.rect.y += self.speed
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
