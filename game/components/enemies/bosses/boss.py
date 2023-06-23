from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, UP, DOWN, BULLET_ENEMY_TYPE
import random

class Boss(Enemy):
    PATTERNS = [0, 1]
    X_POS = (SCREEN_WIDTH // 2)
    Y_POS = 0 
    SHOOTING_TIME = 1000
    MOV_Y = [UP, DOWN]

    def __init__(self, image):
        super().__init__(image)
        self.shooting_interval = self.SHOOTING_TIME
        self.interval = random.randint(100, 1000)
        self.health = 100
        self.pattern = 0
        self.mov_y = random.choice(self.MOV_Y)
        self.is_defeated = False
        self.invincible_ticks = 0
        


    def update(self, bullet_handler):
        if self.is_destroyed:
            self.health -= 5
            self.is_destroyed = False
            self.invincible_ticks = 2

        if self.health <= 0:
            self.is_defeated = True

        if self.invincible_ticks > 0:
            self.invincible_ticks -= 1

        if (self.index % self.interval) == 0:
            self.pattern = random.choice(self.PATTERNS)

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
        pass
    
