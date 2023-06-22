import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2
from random import choice
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT
 
class Spider(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_Y = 3
    SPEED_X = 7
    INTERVAL = 15
    SHOOTING_TIME = 50
    

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    

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
            

