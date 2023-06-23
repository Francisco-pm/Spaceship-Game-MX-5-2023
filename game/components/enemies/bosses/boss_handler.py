import random
from game.components.enemies.bosses.alien_leader import AlienLeader

class BossHandler:
    MAX_BOSSES_PER_SCREEN = 1

    def __init__(self):
        self.bosses = []
        self.bosses_defetead = 0
        self.bosses_defetead_in_round = 0
        self.boss_round = False
        
    def get_list(self):
        return self.bosses
    
    def update(self, bullet_handler, enemy_handler):
        self.add_boss(enemy_handler)
        for boss in self.bosses:
            boss.update(bullet_handler)
            if boss.is_defeated:
                self.bosses_defetead += 1
                self.bosses_defetead_in_round += 1
                self.is_alive = False
                self.remove_boss(boss)
        if self.bosses_defetead_in_round != 0:
            self.boss_round = False
            enemy_handler.enemy_round = True
            self.bosses_defetead_in_round = 0


    def draw(self, screen):
        for boss in self.get_list():
            boss.draw(screen)

    def add_boss(self, enemy_handler):
        if len(self.get_list()) == 0 and self.boss_round and not enemy_handler.enemy_round:
            self.bosses.append(AlienLeader())




    def remove_boss(self, boss):
        self.bosses.remove(boss)
        self.boss_round = False

    def reset(self):
        self.bosses = []
        self.bosses_defetead = 0
        self.bosses_defetead_in_round = 0
