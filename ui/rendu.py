import pygame

class Rendu:
    def __init__(self,grille):
        self.grille = grille
        self.taille_case = 40
        self.hauteur_pixel = grille.hauteur * self.taille_case
        self.largeur_pixel = grille.largeur * self.hauteur_pixel

# pygame.init()




