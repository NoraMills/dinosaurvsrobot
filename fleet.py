from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []  # this is where your fleet goes

    def create_fleet(self):
        i = 0
        robots = []
        robot_names = ["Lore", "Rock Em", "Sock Em"]
        names_of_weapons = ["Lascannon", "Power Sword", "Heavy Bolter"]
        damage_of_weapons = [15, 25, 20]
        while i < 3:
            name = robot_names[i]
            weapon_name = names_of_weapons[i]
            weapon_damage = damage_of_weapons[I]
            robot = Robot(name)
            robot.weapon = Weapon(weapon_name, weapon_damage)
            robots.append(robot)
            i += 1
        self.robots = robots
        pass
