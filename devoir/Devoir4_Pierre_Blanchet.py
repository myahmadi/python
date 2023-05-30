# Créé par pierre.blanchet, le 25/05/2023 en Python 3.7
#ex1
def renverse(mot):
    nouveauMot =""
    for i in range(len(mot)-1,-1,-1):
        nouveauMot+=mot[i]
    return nouveauMot

print(renverse("informatique"))

#ex2

from random import randint
def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ",nb_mystere)

plus_ou_moins()


#ex3
def recherche(lettre,mot):
    compteur=0
    for i in range(len(mot)):
        if lettre == mot[i]:
            compteur +=1
    return compteur

print(recherche('e', "sciences")) #2
print(recherche('i', "mississippi")) #4
print(recherche('a', "mississippi"))#0

#ex4
def correspond(mot,mot_a_trous):
    mot_a_trous_remplacer = ""
    if len(mot)!=len(mot_a_trous):
        return False
    for i in range(len(mot_a_trous)):
        if mot_a_trous[i]=='*':
            mot_a_trous_remplacer+=mot[i]
        else:
            mot_a_trous_remplacer+=mot[i]
    if mot_a_trous_remplacer==mot:
        return True
    else:
        return False
print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) #True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) #False
print(correspond('STOP', 'S*')) #False
print(correspond('AUTO', '*UTO')) #True