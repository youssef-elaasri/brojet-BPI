#!/usr/bin/env python3
"""
le cœur de notre simulation
"""
import sys
from random import uniform
def points(nombre_des_points=int):
    """
    retourn un dictionnaire qui contien les point comme clé et les valeur sons des 0 ou 1
    1 si le point est dans le cercle
    0 si non
    et le nombre total des point dans le cercle de centre (0,0) et de rayon 1
    """
    point = dict()
    nombre_des_points_dans_le_cercle = 0
    for _ in range(nombre_des_points):
        abscisse = uniform(-1,1)
        ordonnee = uniform(-1,1)
        if abscisse**2 + ordonnee**2 <=1:
            nombre_des_points_dans_le_cercle +=1
            point[(abscisse,ordonnee)] = 1
        else:
            point[((abscisse,ordonnee))] = 0
    return point,4*(nombre_des_points_dans_le_cercle/nombre_des_points)
def main():
    """
    affiche la valeur approximative de pi en utilisant le nombre du point donné depuit
    la ligne de commande
    """
    print(points(int(sys.argv[1]))[1])
if __name__ == "__main__":
    main()
