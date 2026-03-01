from grille import Grille
class Robot:
    def __init__(self,grille):
        self.depart = self.depart
        self.x,self.y = self.grille

def commencer(self):
        file = [self.depart]      # la file pour BFS
        parcouru = []             # cases déjà visitées
        parent = {self.depart: None}  # pour reconstruire le chemin

        directions = [(-1,0),(1,0),(0,-1),(0,1)]  # haut, bas, gauche, droite

        while file:
            u = file.pop(0)       
            parcouru.append(u)

            if u == self.arrivee:
                
                chemin = []
                while u is not None:
                    chemin.append(u)
                    u = parent[u]
                chemin.reverse()
                return chemin

            x, y = u
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                case = (nx, ny)
                if 0 <= nx < self.hauteur and 0 <= ny < self.largeur:
                    if self.grille[nx][ny] == 1 and case not in parcouru and case not in file:
                        file.append(case)
                        parent[case] = u

        return None  # pas de chemin trouvé
