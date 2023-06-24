import pygame 
import random
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE, SPACESHIP_SHIELD, RESET, SPACESHIP_BLINK1, SPACESHIP_BLINK2, SPACESHIP_BLINK3
from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.components.power_ups.shield import Shield




class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH 
    Y_POS = (SCREEN_HEIGHT // 2) + HEIGHT
    SHOOTING_TIME = 6
    SPEED = 15
    HITS = 3
    INVINCIBLE_TICKS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_destroyed = False
        self.is_alive = True
        self.shooting_time = 0
        self.hits = self.HITS
        self.invincible = False
        self.invincible_ticks = 0
        self.shielded = False
        self.time_up = 0

    def update(self, user_input, bullet_handler, enemy_handler, boss_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)

        if self.shielded:
            time_left = round((self.time_up - pygame.time.get_ticks())/1000, 2)
            if time_left < 0:
                self.desactivate_power_up()

        if self.invincible:
            invencible_time = round((self.invincible_ticks - pygame.time.get_ticks())/1000, 2)
            if invencible_time < 0:
                self.invincible = False


        self.collide(enemy_handler.get_list())
        self.collide(boss_handler.get_list())

        if self.hits == 0:
            self.is_alive = False

    def draw(self, screen):
        if self.invincible:
            self.image = random.choice([SPACESHIP_BLINK1, SPACESHIP_BLINK3])
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        elif self.shielded:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH +10, self.HEIGHT + 10))
        else:
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
            
        screen.blit(self.image, self.rect)
        
    def get_hit(self):
        self.hits -= 1
        self.invincible_ticks = pygame.time.get_ticks() + self.INVINCIBLE_TICKS
        self.invincible = True

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.SPEED
        
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.SPEED

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.SPEED

    def move_up(self):
        if self.rect.top > (SCREEN_HEIGHT // 2):
            self.rect.y -= self.SPEED

    def shoot(self, bullet_handler):
        if (self.shooting_time % self.SHOOTING_TIME) == 0:
            bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)
        self.shooting_time += 1

    def collide(self, objects):
        if not (self.invincible or self.shielded):
            for object in objects:
                if self.rect.colliderect(object.rect):
                    object.is_destroyed = True
                    self.is_destroyed = True
                    self.get_hit()

    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.shielded = True


    def desactivate_power_up(self, reset=None):
        if reset is None:
            self.shielded = False
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        else:
            self.shielded = False
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        
    def reset(self):
        self.rect.x = self.X_POS
        self.desactivate_power_up(RESET)
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.hits = self.HITS
        self.is_destroyed = False
        self.invincible = 0
        self.invincible_ticks = 0