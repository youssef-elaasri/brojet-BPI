"""
    génération de notre image animée représentant une simulation
"""
import sys
import subprocess
from approximate_pi import points

def ecrire(nombre,liste_image,ordre):
    """
    ecritr le nombre dans la liste_image qui représente notre image
    le nombre peut etre .
    ordre : par exemble si en a 3.145, 3 est de l'ordre 0, . est de l'ordre 1, 1 de l'ordre 2 ....
    """
    largeur_un_nombre = len(liste_image)//15
    hauteur_un_nomre = len(liste_image)//11
    if nombre == ".":
        for indice_ligne in range(6*hauteur_un_nomre-hauteur_un_nomre//8,6*hauteur_un_nomre):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(6+ordre)*largeur_un_nombre +largeur_un_nombre//5 ):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "1":
        for indice_ligne in range(5*hauteur_un_nomre,6*hauteur_un_nomre):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(6+ordre)*largeur_un_nombre +largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "2":
        for indice in [5*hauteur_un_nomre,(11*hauteur_un_nomre)//2,6*hauteur_un_nomre - hauteur_un_nomre//8]:
            for indice_ligne in range(indice,indice+hauteur_un_nomre//8):
                for indice_pixel in range((6+ordre)*largeur_un_nombre,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                    liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range(5*hauteur_un_nomre,(11*hauteur_un_nomre)//2):
            for indice_pixel in range((7+ordre)*largeur_un_nombre - 2*largeur_un_nombre//5,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range((11*hauteur_un_nomre)//2,6*hauteur_un_nomre):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(6+ordre)*largeur_un_nombre + largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "3":
        for indice in [5*hauteur_un_nomre,(11*hauteur_un_nomre)//2,6*hauteur_un_nomre - hauteur_un_nomre//8]:
            for indice_ligne in range(indice,indice+hauteur_un_nomre//8):
                for indice_pixel in range((6+ordre)*largeur_un_nombre,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                    liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range(5*hauteur_un_nomre,6*hauteur_un_nomre):
            for indice_pixel in range((7+ordre)*largeur_un_nombre - 2*largeur_un_nombre//5,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "4":
        for indice_ligne in range(5*hauteur_un_nomre,6*hauteur_un_nomre):
            for indice_pixel in range((7+ordre)*largeur_un_nombre - 2*largeur_un_nombre//5,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range((11*hauteur_un_nomre)//2,(11*hauteur_un_nomre)//2+hauteur_un_nomre//8):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range(5*hauteur_un_nomre,(11*hauteur_un_nomre)//2):
            for indice_pixel in range((6+ordre)*largeur_un_nombre ,(6+ordre)*largeur_un_nombre + largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "5":
        for indice_ligne in range(5*hauteur_un_nomre,(11*hauteur_un_nomre)//2):
            for indice_pixel in range((6+ordre)*largeur_un_nombre ,(6+ordre)*largeur_un_nombre + largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range((11*hauteur_un_nomre)//2,6*hauteur_un_nomre):
            for indice_pixel in range((7+ordre)*largeur_un_nombre - 2*largeur_un_nombre//5,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice in [5*hauteur_un_nomre,(11*hauteur_un_nomre)//2,6*hauteur_un_nomre - hauteur_un_nomre//8]:
            for indice_ligne in range(indice,indice+hauteur_un_nomre//8):
                for indice_pixel in range((6+ordre)*largeur_un_nombre,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                    liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "6":
        ecrire("5",liste_image,ordre)
        for indice_ligne in range((11*hauteur_un_nomre)//2,6*hauteur_un_nomre):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(6+ordre)*largeur_un_nombre + largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "7":
        for indice_ligne in range(5*hauteur_un_nomre,6*hauteur_un_nomre):
            for indice_pixel in range((7+ordre)*largeur_un_nombre - 2*largeur_un_nombre//5,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
        for indice_ligne in range(5*hauteur_un_nomre,5*hauteur_un_nomre+hauteur_un_nomre//8):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "8":
        ecrire("3",liste_image,ordre)
        ecrire("1",liste_image,ordre)
    if nombre == "9":
        ecrire("5",liste_image,ordre)
        for indice_ligne in range(5*hauteur_un_nomre,(11*hauteur_un_nomre)//2):
            for indice_pixel in range((7+ordre)*largeur_un_nombre - 2*largeur_un_nombre//5,(7+ordre)*largeur_un_nombre - largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "
    if nombre == "0":
        ecrire("7",liste_image,ordre)
        ecrire("1",liste_image,ordre)
        for indice_ligne in range(6*hauteur_un_nomre - hauteur_un_nomre//8,6*hauteur_un_nomre):
            for indice_pixel in range((6+ordre)*largeur_un_nombre,(7+ordre)*largeur_un_nombre-largeur_un_nombre//5):
                liste_image[indice_ligne][indice_pixel] = "0 0 0 "

def generate_ppm_file(numero_image,nombre_des_points):
    """
    génère une image au format PPM.
    L'image doit montrer les points qui sont à l'intérieur du cercle d'une certaine couleur,
    les points qui sont à l'extérieur du cercle d'une autre couleur
    et la valeur approchée de π
    """
    dimension = int(sys.argv[1])
    points_data = points(nombre_des_points)[0]
    approximate_pi = str(points(nombre_des_points)[1])[:int(sys.argv[3])+2]
    liste_image = [["255 255 255 " for _ in range(dimension)] for _ in range(dimension)]
    for point in points_data.items():
        abscisse = point[0][0]
        ordonnee = point[0][1]
        if point[1] == 1:
            liste_image[int((dimension//2)*(1+abscisse))][int((dimension//2)*(1-ordonnee))] = "255 0 0 "
        else:
            liste_image[int((dimension//2)*(1+abscisse))][int((dimension//2)*(1-ordonnee))] = "0 255 0 "
    pi_iter = iter(approximate_pi)
    for ordre,nombre in enumerate(pi_iter):
        ecrire(nombre,liste_image,ordre)
    fichier = open(f"img{numero_image}_{approximate_pi[0]}-{approximate_pi[1:]}.ppm","w",encoding="utf-8")
    fichier.write("P3\n")
    fichier.write(str(dimension) + " " + str(dimension) + "\n")
    fichier.write("255\n")
    for ligne in liste_image:
        fichier.writelines(ligne)
        fichier.write("\n")
    fichier.close()
for i in range(10):
    generate_ppm_file(i,int(sys.argv[2])//(10-i))
subprocess.run('convert -delay 100 -loop 0 *.ppm approximation.gif',shell=True,check=True)
