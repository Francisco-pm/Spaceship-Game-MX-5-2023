from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import random

class PowerUp:
    WIDTH = 30
    HEIGHT = 30
    POS_Y = 0
    SPEED_Y = 5
    TIME_UP = 5000

    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = self.POS_Y
        self.is_alive = True
        self.is_used = False
        self.time_up = 0

    def update(self, player):
        self.rect.y += self.SPEED_Y
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        if self.rect.colliderect(player.rect):
            self.is_alive = False
            self.is_used = True
            self.time_up = pygame.time.get_ticks() + self.TIME_UP

    def draw(self, screen):
        screen.blit(self.image, self.rect)
