from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, SCREEN_HEIGHT
import pygame

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH , self.HEIGHT))
        super().__init__(self.image, center)

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
        self.rect.y += self.SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.is_alive = False
        