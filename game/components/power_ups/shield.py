from game.components.power_ups.PowerUp import PowerUp
from game.utils.constants import SHIELD

class Shield(PowerUp):
    
    def __init__(self):
        self.image = SHIELD
        super().__init__(self.image)

    