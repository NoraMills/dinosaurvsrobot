from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaur = []

    def create_herd(self):
        i = 0
        dinosaurs = []
        dinosaur_names = ["Rex Shortarm", "Michael Cera'Tops", "Longneck"]
        damage_of_dinosaurs = [15, 25, 20]
        while i < 3:
            name = dinosaur_names[i]
            dinosaur_damage = damage_of_dinosaurs[i]
            dinosaur = Dinosaur(name, dinosaur_damage)
            dinosaurs.append(dinosaur)
            i += 1
        self.dinosaurs = dinosaurs
        pass
