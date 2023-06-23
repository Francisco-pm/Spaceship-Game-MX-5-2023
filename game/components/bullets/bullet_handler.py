from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_SPACESHIP_TYPE, BULLET_BOSS_TYPE, DOWN
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bulletboss import BulletBoss
from game.components.bullets.bullet_spaceship import BulletSpaceship

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies, bosses):
        for bullet in self.get_list():
            if type(bullet) is BulletEnemy:
                bullet.update(player)
            elif type(bullet) is BulletBoss:
                bullet.update(player)
            elif type(bullet) is BulletSpaceship:
                for enemy in enemies:
                    bullet.update(enemy)
                for boss in bosses:
                    bullet.update(boss)

            self.remove_bullet(bullet)
            

    def get_list(self):
        return self.bullets

    def draw(self, screen):
        for bullet in self.get_list():
            bullet.draw(screen)

    def add_bullet(self, type, center, direction=DOWN):
        if type == BULLET_BOSS_TYPE:
            self.bullets.append(BulletBoss(center, direction))
        elif type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_SPACESHIP_TYPE:
            self.bullets.append(BulletSpaceship(center))

    def remove_bullet(self, bullet):
        if not bullet.is_alive:
            self.bullets.remove(bullet)

    def reset(self):
        self.bullets = []