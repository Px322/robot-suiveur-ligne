import pygame

class Rendu:
    def __init__(self,grille):
        self.grille = grille
        self.taille_case = 40
        self.hauteur_pixel = grille.hauteur * self.taille_case
        self.largeur_pixel = grille.largeur * self.hauteur_pixel

        self.fenetre = pygame.display.set_mode((self.largeur_pixel, self.hauteur_pixel))
        pygame.display.set_caption("Robot - BFS")

        
        self.BLANC = (255, 255, 255)
        self.NOIR = (0, 0, 0)
        self.VERT = (0, 200, 0)    # chemin
        self.ROUGE = (200, 0, 0)   # arrivée
        self.BLEU = (0, 0, 200)    # départ
        self.JAUNE = (255, 220, 0) # solution BFS

        def dessiner(self, chemin=None):


