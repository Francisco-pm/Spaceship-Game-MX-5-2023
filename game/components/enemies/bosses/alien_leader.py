from game.components.enemies.bosses.boss import Boss
from game.utils.constants import BOSS_1
import pygame

class AlienLeader(Boss):
    WIDTH = 200
    HEIGHT = 250


    def __init__(self):
        self.image = BOSS_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)