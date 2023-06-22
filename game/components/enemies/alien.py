from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3, SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT

import pygame

class Alien(Enemy):
    WIDTH = 45
    HEIGHT = 30
    SPEED_Y = 10
    SPEED_X = 10
    INTERVAL = 15
    SHOOTING_TIME = 1000
    
    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

    def move(self):

        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.rect.left <= 0:
                self.mov_x = RIGHT
                self.rect.y += self.SPEED_Y

        else:
            self.rect.x += self.SPEED_X
            if self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT
                self.rect.y += self.SPEED_Y
 

