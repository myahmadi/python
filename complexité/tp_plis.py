from pylab import *
EPAISSEUR_FEUILLE=0.0001

def calcul_nb_pliages(hauteur):
    x=[]
    y=[]
    somme_hauteur=EPAISSEUR_FEUILLE
    pliages=0
    while (somme_hauteur<hauteur):
        somme_hauteur = somme_hauteur*2
        pliages += 1
        x.append(somme_hauteur)
        y.append(pliages)


        print(somme_hauteur)
    return pliages
    pylab.plot(x, y)
    pylap.show()  # affiche la figure à l'écran

print(calcul_nb_pliages(384400000))