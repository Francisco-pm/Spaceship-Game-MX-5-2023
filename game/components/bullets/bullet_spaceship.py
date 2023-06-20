from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_PLAYER_TYPE
import pygame

class BulletSpaceship(Bullet):
    WIDTH = 8
    HEIGHT = 25
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH , self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, enemy):
        self.rect.y -= self.SPEED

        if self.rect.y <= 0:
            self.is_alive = False
        
        if not enemy.TYPE == BULLET_PLAYER_TYPE:
            if self.rect.colliderect(enemy.rect):
                enemy.is_alive = False
                self.is_alive = False