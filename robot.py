class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(self.name + " has attacked. " + self.weapon.attack_power +
              " damage was done to " + dinosaur.name)
