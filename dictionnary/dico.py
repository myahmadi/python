# Créé par PIERRE.BLANCHET, le 07/02/2023 en Python 3.7
"""
import csv


fichier = open("test.csv", "r")


lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_personnes = []
for ligne in lecture_fichier:
    liste_personnes.append(dict(ligne))
fichier.close()

for personne in liste_personnes :
    print(personne)
"""
#ex 7
import csv
from pylab import *


def listePourUneCle(liste_dico, cle):
    resultat=[]
    for dico in liste_dico:
        resultat.append(float(dico[cle]))
    return resultat


fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')
liste_enregistrements = []
for ligne in lecture_fichier:
    liste_enregistrements.append(dict(ligne))
fichier.close()

#a compléter
liste_altitudes = listePourUneCle(liste_enregistrements,"Altitude m")
liste_pression = listePourUneCle(liste_enregistrements,"Pression mb")
x = liste_altitudes
y = liste_pression
plot(x,y)
show()



