from game.components.enemies.ship import Ship
from game.components.enemies.spider import Spider
from game.components.enemies.alien import Alien
from random import choice

class EnemyHandler:
    SPAWN_RATE = 50
    BOSS_SPAWN_RATE = 5
    def __init__(self):
        self.enemies = []
        self.counter = 1
        self.number_enemies_destroyed = 0
        self.number_enemies_destroyed_in_round = 0
        self.enemy_round = True
        self.spawn_rate = self.SPAWN_RATE
    
    def get_list(self):
        return self.enemies

    def update(self, bullet_handler, boss_handler):
        

        self.add_enemy()

        if self.number_enemies_destroyed_in_round >= self.BOSS_SPAWN_RATE:
                self.enemy_round = False
                self.number_enemies_destroyed_in_round = 0

        if self.enemy_round:

            for enemy in self.enemies:
                enemy.update(bullet_handler)
                if enemy.is_destroyed:
                    self.number_enemies_destroyed += 1
                    self.number_enemies_destroyed_in_round += 1
                    self.counter += 1
                    enemy.is_alive = False
                if not enemy.is_alive:
                    self.remove_enemy(enemy)

    
        else:
            self.enemies = []
            boss_handler.boss_round = True

        
            
    def draw(self, screen):
        for enemy in self.get_list():
            enemy.draw(screen)

    def add_enemy(self):
        if ((self.counter % self.spawn_rate) == 0 or len(self.enemies) <= 0) and len(self.enemies) < 8:
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
        self.number_enemies_destroyed_in_round = 0
