import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2
from random import choice
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT
 
class Spider(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.SPEED_Y = 3
        self.SPEED_X = 7
        self.INTERVAL = 15
        self.is_alive = True

    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.left <= 0:
                self.mov_x = choice(self.MOV_X)
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.mov_x = choice(self.MOV_X)
                self.index = 0
        self.index += 2
            

