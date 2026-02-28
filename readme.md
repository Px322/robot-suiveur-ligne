# Robot suiveur de ligne (simulation)

## Description

Ce projet consiste à simuler un robot capable de suivre une ligne noire sur une grille.

La grille est générée à partir d’un fichier **JSON** contenant la taille, le point de départ et le point d’arrivée
Un chemin composé de `1` est créé aléatoirement entre ces deux points (les `1` se suivent logiquement pour permettre le déplacement du robot).

L’objectif est ensuite d’afficher cette grille avec **Pygame** afin d'avoir une inteface utilisateur pour voir le robot se déplacer

---

## Fonctionnement

* Lecture des paramètres depuis un fichier JSON
* Génération d’une grille remplie de `0`
* Création d’un chemin aléatoire continu de `1` entre départ et arrivée
* Déplacement du robot uniquement sur les cases contenant `1`
* Affichage graphique avec Pygame 

---

## Technologies utilisées

* Python — langage principal
* JSON — configuration de la grille
* random — génération du chemin aléatoire
* Pygame — affichage graphique et animation du robot

---

## Installation

Installer la dépendance :

```
pip install pygame
```

Puis exécuter le script principal.

---

## Objectif du projet

* Manipuler des matrices en Python
* Comprendre la génération de chemin logique
* Simuler un déplacement automatique
* Découvrir Pygame

---

## Améliorations possibles

* Génération d’un chemin plus complexe
* Version avec capteurs simulés comme un vrai robot
