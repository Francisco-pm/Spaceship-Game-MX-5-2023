from game.components.power_ups.shield import Shield

class PowerUpHandler:
    INTERVAL = 300

    def __init__(self):
        self.power_ups = []
        self.interval = 0

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
        self.interval += 1
    
    def draw(self, screen):
        for power_up in self.get_list():	
            power_up.draw(screen)

    def add_power_up(self):
        if (self.interval % self.INTERVAL) == 0:
            self.power_ups.append(Shield())
            

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)

    def reset(self):
        self.power_ups = []
        self.interval = 0