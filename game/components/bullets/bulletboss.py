from game.components.bullets.bullet import Bullet
from game.utils.constants import UP, DOWN,RIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY
import pygame

class BulletBoss(Bullet):
    WIDTH = 15
    HEIGHT = 50
    SPEED = 20
    def __init__(self, center, direction):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH , self.HEIGHT))
        super().__init__(self.image, center)
        self.direction = direction

    def update(self, player):
        self.move()
        if self.rect.colliderect(player.rect):
            if player.invincible or player.shielded:
                self.is_alive = False
            else:
                player.is_destroyed = True
                player.get_hit()
                self.is_alive = False

    def move(self):
        if self.direction == UP:
            self.rect.y -= self.SPEED 
            if self.rect.y <= 0:
                self.is_alive = False
        elif self.direction == DOWN:
            self.rect.y += self.SPEED
            if self.rect.y > SCREEN_HEIGHT:
                self.is_alive = False

        