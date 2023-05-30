# Créé par PIERRE.BLANCHET, le 14/03/2023 en Python 3.7
import os
fichier=open("texte.txt","w")
fichier.write("bonjour\n")
fichier.write("salut")
fichier.close()


fichier=open("texte.txt","a")
fichier.write("hasta luego")
fichier.close()

fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()