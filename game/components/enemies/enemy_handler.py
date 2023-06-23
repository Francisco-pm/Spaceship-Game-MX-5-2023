from game.components.enemies.ship import Ship
from game.components.enemies.spider import Spider
from game.components.enemies.alien import Alien
from random import choice

class EnemyHandler:
    SPAWN_RATE = 50

    def __init__(self):
        self.enemies = []
        self.counter = 1
        self.number_enemies_destroyed = 0
        self.difficulty_meter = 1
        self.spawn_rate = self.SPAWN_RATE
    
    def get_list(self):
        return self.enemies

    def update(self, bullet_handler, boss_handler):
        
        if not len(boss_handler.bosses) > 0:
            self.add_enemy()

            for enemy in self.get_list():
                enemy.update(bullet_handler)
                if enemy.is_destroyed:
                    self.number_enemies_destroyed += 1
                    self.counter += 1
                    self.difficulty_meter += 1
                    enemy.is_alive = False
                if not enemy.is_alive:
                    self.remove_enemy(enemy)
            if (self.difficulty_meter % 10) == 0:
                if self.spawn_rate > 10:
                    self.spawn_rate -= 20
                    self.difficulty_meter = 1
                elif self.spawn_rate < 21:
                    self.spawn_rate = 10
                    self.difficulty_meter = 1
        else:
            self.enemies = []
            
    def draw(self, screen):
        for enemy in self.get_list():
            enemy.draw(screen)

    def add_enemy(self):
        if ((self.counter % self.spawn_rate) == 0 or len(self.enemies) < 1) and len(self.enemies) < 8:
            self.enemies.append(choice((Ship(), Spider(), Alien())))
            self.counter += 1
        else:
            self.counter += 1


    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0
        self.spawn_rate = self.SPAWN_RATE
        self.counter = 1
        self.difficulty_meter = 1
