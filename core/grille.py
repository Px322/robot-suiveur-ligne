import json
import random

class Grille:

    def __init__(self,grille_path):
            with open(grille_path, 'r') as f:
                data = json.load(f)
            self.hauteur,self.largeur = data["grille"]
            self.depart = data["depart"]
            self.arrivee = data["arrivee"]

            self.grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]

    def creer_chemin(self):
        x, y = self.depart
        self.grille[x][y] = 1

        while [x, y] != self.arrivee:
            directions = []

            if x < self.arrivee[0]:
                directions.append((1, 0))
            if x > self.arrivee[0]:
                directions.append((-1, 0))
            if y < self.arrivee[1]:
                directions.append((0, 1))
            if y > self.arrivee[1]:
                directions.append((0, -1))

            dx, dy = random.choice(directions)
            x += dx
            y += dy

            self.grille[x][y] = 1