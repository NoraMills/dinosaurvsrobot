from dinosaur import Dinosaur
import random


class Herd:
    def __init__(self):
        self.dinosaur = []

    def create_herd(self):
        i = 0
        dinosaurs = []
        dinosaur_names = ["Rex Shortarm", "Michael Cera'Tops", "Longneck"]
        damage_of_dinosaurs = [random.randrange(
            8, 13), random.randrange(10, 25), random.randrange(2, 10)]
        while i < 3:
            name = dinosaur_names[i]
            dino_damage = damage_of_dinosaurs[i]
            dinosaur = Dinosaur(name, dino_damage)
            dinosaurs.append(dinosaur)
            i += 1
        self.dinosaurs = dinosaurs
        pass
