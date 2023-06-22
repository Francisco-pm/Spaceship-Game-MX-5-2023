import pygame 
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE
from game.components.bullets.bullet_spaceship import BulletSpaceship




class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH 
    Y_POS = (SCREEN_HEIGHT // 2) + HEIGHT
    SHOOTING_TIME = 6
    SPEED = 15

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0

    def update(self, user_input, bullet_handler, enemy_handler):
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

        self.collide(bullet_handler.get_list())
        self.collide(enemy_handler.get_list())

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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
        if not (type(objects) is Spaceship):
            for object in objects:
                if not (type(object) is BulletSpaceship):
                    if self.rect.colliderect(object.rect):
                        object.is_alive = False
                        self.is_alive = False

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True