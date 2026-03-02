
from core.grille import Grille
from core.robot import Robot

grille1 = Grille("data/grille.json")
grille1.creer_chemin()

# affiche la grille
for ligne in grille1.grille:
    print(" ".join(str(c) for c in ligne))

Paul = Robot(grille1)
chemin = Paul.commencer()

print("\nChemin trouvé par le robot :")
print(chemin)

