import json

class Grille:

    def __init__(self,grille_path):
            with open(grille_path, 'r') as f:
                data = json.load(f)
            self.hauteur,self.largeur = data["grille"]
            self.depart = data["depart"]
            self.arrivee = data["arrivee"]

            self.grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]