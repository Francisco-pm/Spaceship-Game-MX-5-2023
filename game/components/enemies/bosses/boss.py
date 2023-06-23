from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, UP, DOWN, BULLET_BOSS_TYPE
import pygame
import random

class Boss(Enemy):
    PATTERNS = [0, 1]
    X_POS = (SCREEN_WIDTH // 2)
    Y_POS = 0 
    SHOOTING_TIME = 20
    MOV_Y = [UP, DOWN]
    INTERVAL = 500

    def __init__(self, image):
        super().__init__(image)
        self.shooting_time = 0
        self.health = 100
        self.pattern = 0
        self.mov_y = random.choice(self.MOV_Y)
        self.is_defeated = False
        


    def update(self, bullet_handler):
        if self.is_destroyed:
            self.health -= 5
            self.is_destroyed = False

        if self.health <= 0:
            self.is_defeated = True


        if (self.index % self.INTERVAL) == 0:
            if self.pattern == 0:
                self.pattern = 1
            else:
                self.pattern = 0
            self.index = 0

        self.move()
        self.shoot(bullet_handler)
        self.shooting_time += 1
        
    def move(self):
        if self.pattern == 0:
            if self.mov_y == UP:
                self.rect.y -= self.SPEED_Y
                if self.rect.y < 0:
                    self.mov_y = DOWN
            else:
                self.rect.y += self.SPEED_Y
                if self.rect.right > SCREEN_HEIGHT:
                    self.mov_y = UP

            if self.mov_x == LEFT:
                self.rect.x -= self.SPEED_X
                if self.rect.left <= 0:
                    self.mov_x = RIGHT
                    
            else:
                self.rect.x += self.SPEED_X
                if self.rect.right >= SCREEN_WIDTH:
                    self.mov_x = LEFT
            self.index += 1
                    
        elif self.pattern == 1:
            if self.mov_x == LEFT:
                self.rect.x -= self.SPEED_X
                if self.rect.left <= 0:
                    self.mov_x = RIGHT
                    
            else:
                self.rect.x += self.SPEED_X
                if self.rect.right >= SCREEN_WIDTH:
                    self.mov_x = LEFT
            self.index -= 1
        
    
    def shoot(self, bullet_handler):
        bullet = self.rect.copy()
        bullet_1 = bullet.center = (self.rect.left, self.rect.centery)
        bullet_2 = bullet.center = (self.rect.right, self.rect.centery)

        if (self.shooting_time % self.SHOOTING_TIME) == 0:
            if self.pattern == 0:
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, self.rect.center, DOWN)
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, self.rect.center, UP)

            elif self.pattern == 1:
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, self.rect.center, UP)
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, bullet_1, UP)
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, bullet_2, UP)
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, self.rect.center, DOWN)
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, bullet_1, DOWN)
                bullet_handler.add_bullet(BULLET_BOSS_TYPE, bullet_2, DOWN)
        
