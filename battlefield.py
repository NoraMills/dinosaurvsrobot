from herd import Herd
from fleet import Fleet
import random


class Battlefield:
    def __init__(self):
        self.Fleet = None
        self.Herd = None

    def run_game(self):
        fleet = Fleet()
        herd = Herd()
        turn_one = self.display_welcome()
        self.display_welcome()
        fleet.create_fleet()
        herd.create_herd()
        self.fleet = fleet
        self.herd = herd
        winner = None
        game_state = True
        while game_state:
            if turn_one == 1:
                self.robo_turn()
                self.dino_turn()
            else:
                self.dino_turn()
                self.robo_turn()
            if self.fleet.robots[0].health <= 0:
                print(self.fleet.robots[0].name + " has fallen.")
                self.fleet.robots.remove(self.fleet.robots[0])
            if self.herd.dinosaurs[0].health <= 0:
                print(self.herd.dinosaurs[0].name +
                      " an extinction level event has occurred.")
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
            if len(self.fleet.robots) < 1:
                winner = "Dinosaurs have made a dent in waste!"
                game_state = False
            if len(self.herd.dinosaurs) < 1:
                winner = "Robots were victorious against the meat bags!"
                game_state = False
        self.display_winners(winner)

    def display_welcome(self):
        print("Welcome to the Dunderthdome! Two may enter, only one may leave. Get ready to fight!")
        first_turn = random.randrange(1, 2)
        if first_turn == 1:
            print("Robots won the coin toss!\n")
        else:
            print("Dinosaurs won the coin toss!\n")
        return first_turn

    def battle(self):

        # this is better as part of the wecome
        # first_turn = random.randint(1, 2)
        # if first_turn == 1:
        #     print("Robots won the coin toss!")
        #     first_turn = 1
        # if first_turn == 2:
        #     print("Dinosaurs won the coin toss!")
        #     first_turn = 2
        # this was just longer than it needed to be.
        # if first_turn == 1:
        #     while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
        #         if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

        #             self.robo_turn()  # First team turn?

        #             if self.herd.dinosaurs[0].health <= 0:
        #                 print(f'{self.herd.dinosaurs[0].type} is out.')
        #                 self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
        #             elif self.fleet.robots[0].health <= 0:
        #                 print(f'{self.fleet.robots[0].name} is out.')
        #                 self.fleet.robots.remove(self.fleet.robots[0])
        #             if len(self.fleet.robots) == 0:
        #                 self.display_winners_dinosaurs()
        #                 return
        #             elif len(self.herd.dinosaurs) == 0:
        #                 self.display_winners_robots()
        #                 return
        #             self.dino_turn()  # Second teams turn?

        #             if self.herd.dinosaurs[0].health <= 0:
        #                 print(f'{self.herd.dinosaurs[0].type} is out.')
        #                 self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
        #             elif self.fleet.robots[0].health <= 0:
        #                 print(f'{self.fleet.robots[0].name} is out.')
        #                 self.fleet.robots.remove(self.fleet.robots[0])

        #             if len(self.fleet.robots) == 0:
        #                 self.display_winners_dinosaurs()
        #                 return
        #             elif len(self.herd.dinosaurs) == 0:
        #                 self.display_winners_robots()
        #                 return

    def dino_turn(self, dinosaur):
        self.herd.dinosaurs[0].attack(self.fleet.robots[0])

    def robo_turn(self, robot):
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self, winner):
        print(winner)
