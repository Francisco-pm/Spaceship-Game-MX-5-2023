class AlienLeader(boss):
    
    def __init__(self):
        self.image = BOSS_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)