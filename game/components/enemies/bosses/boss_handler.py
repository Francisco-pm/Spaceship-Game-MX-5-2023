import random
from game.components.enemies.bosses.alien_leader import AlienLeader

class BossHandler:
    MAX_BOSSES_PER_SCREEN = 1

    def __init__(self):
        self.bosses = []
        self.bosses_defetead = 0
        
    def get_list(self):
        return self.bosses
    
    def update(self, bullet_handler, round):
        self.add_boss(round)
        for boss in self.get_list():
            boss.update(bullet_handler)
            if boss.is_defeated:
                self.bosses_defetead += 1
                self.is_alive = False
                self.remove_boss(boss)


    def draw(self, screen):
        for boss in self.get_list():
            boss.draw(screen)

    def add_boss(self, round):
        if round == 2 and len(self.get_list()) < self.MAX_BOSSES_PER_SCREEN:
            self.bosses.append(AlienLeader())

    def remove_boss(self, boss):
        self.bosses.remove(boss)

    def reset(self):
        self.bosses = []
        self.bosses_defetead = 0
