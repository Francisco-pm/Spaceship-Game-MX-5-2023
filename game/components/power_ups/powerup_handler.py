from game.components.power_ups.shield import Shield
import random

class PowerUpHandler:
    INTERVAL = 500

    def __init__(self):
        self.power_ups = []
        self.interval = self.INTERVAL
        self.counter

    def get_list(self):
        return self.power_ups

    def update(self, player):
        self.add_power_up()
        for power_up in self.get_list():
            power_up.update(player)
            if power_up.is_used:
                player.activate_power_up(power_up)

            if not (power_up.is_alive):
                self.remove_power_up(power_up)
        self.counter += 1
    
    def draw(self, screen):
        for power_up in self.get_list():	
            power_up.draw(screen)

    def add_power_up(self):
        if (self.counter % self.interval) == 0:
            self.power_ups.append(Shield())
            self.interval = random.randint(100, 2000)

        
            

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)

    def reset(self):
        self.power_ups = []
        self.interval = self.INTERVAL