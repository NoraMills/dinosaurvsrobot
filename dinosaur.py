class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        print(self.name + " has attacked. " + str(self.attack_power) +
              " damage was done to " + robot.name)
