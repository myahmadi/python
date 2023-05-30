from random import *
from math import sqrt
"""
#ex1

for n in range(1,16,1):
    print(n)



#ex2

for n in range(15,-1,-1):
    print(n)



#ex3
debut = int(input("Votre valeur du début"))
print(debut)
fin = int(input("Votre valeur du fin"))
print(fin)
for n in range(debut,fin + 1):
    print(n)




#ex4
debut = int(input("Votre valeur du début"))
print(debut)
for n in range(debut + 1,fin + 1):
    print(n)


#ex5
debut = int(input("Votre valeur du début"))
for n in range(0,11):
    print(n, " * ", debut, " = ", n*debut)


#ex6
max=0
for n in range(5):
   nb = int(input("Entrez un nombre"))
   if nb>max:
    max=nb
print("le nombre le plus grand est",max)


#ex7
max=0
n=0
while n >= 0:
   nb = int(input("Entrez un nombre"))
   n = nb
   if nb>max:
    max=nb
print("le nombre le plus grand est",max)


#ex8
valeur = 0
somme = 0
while valeur>=0:
    valeur = int(input("Choisir nombre "))
    somme = somme + valeur
print("La somme des nombres est ", somme)



#ex9
menu = "0"
while menu != "q":
    print("1 : charger le fichier")
    print("2 : sauvegarder le fichier")
    print("3 : afficher les données")
    print("4 : modifier les données")
    print("q : quitter")
    print("votre choix ?")
    menu = input("Votre choix ")
    if menu =="1":
        print("Chargement")
    elif menu== "2":
        print("Sauvegarde")
    elif menu== "3":
	    print("Affichage")
    elif menu== "4":
        print("modification")
    elif menu== "q":
        print("Au revoir")
    else:
    	print("erreur")


#10
nombre = randint(1,20)
valeur = 0
while valeur != nombre:
    valeur = int(input("votre chiffre ? "))
    if valeur>nombre:
        print("Chiffre grand")
    elif valeur<nombre:
        print("Chiffre trop petit")
    else:
        print("exact")


#11
nombre = randint(1,20)
valeur = 0
coups = 0
while valeur != nombre:
    coups = coups + 1
    valeur = int(input("votre chiffre ? "))
    if valeur>nombre:
        print("Chiffre grand")
    elif valeur<nombre:
        print("Chiffre trop petit")
    else:
        print("exact vous avez trouvé en ", coups," coups !")

"""

#12
def jeu():
    nombre = randint(1,20)
    valeur = 0
    coups = 0
    while valeur != nombre:
        coups = coups + 1
        valeur = int(input("votre chiffre ? "))
        if valeur>nombre:
            print("Chiffre grand")
        elif valeur<nombre:
            print("Chiffre trop petit")
        else:
            print("exact vous avez trouvé en ", coups," coups !")
            relancer()

def relancer():
    rep = input("Voulez vous rejouer O/N")
    while rep!="O" and rep!="N":
        rep = input("Voulez vous rejouer O/N")
    if rep == "O":
        jeu()
    elif rep == "N":
        print("Dommage")

jeu()

"""
#13

xA = int(input("xA ?"))
yA = int(input("yA ?"))
xB = int(input("xB ?"))
yB = int(input("yB ?"))
AB = sqrt((xB - xA)**2+(yB - yA)**2)
print(AB)
"""