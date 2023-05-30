semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jourDepart=6

for i in range(1,32):
    print("{0:10} {1:2} decembre" .format(semaine[jourDepart],i))
    jourDepart=(jourDepart+1)%7




voyelle=["a","e","i","o","u","y"]
def compteVoyelle(chaine):
    compteur = 0
    for n in range(len(voyelle)):
        compteur=compteur+chaine.count(voyelle[n])
    return compteur



chaine="Je m'appelle Pedro"
print(compteVoyelle(chaine))


def insertion(chaine):
    nouveauMot=""
    for v in range(len(chaine)-1):
        nouveauMot+=chaine[v]+"*"
    nouveauMot+=chaine[-1]
    return nouveauMot


print(insertion(chaine))

def inversionMot(chaine):
    nouveauMot=""
    for a in range(len(chaine)-1,-1,-1):
        nouveauMot+= chaine[a]
    return nouveauMot

mot="Pedro"
print(inversionMot(mot))


semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jourDepart=6

for i in range(1,32):
    print("{0:10} {1:2} decembre" .format(semaine[jourDepart],i))
    jourDepart=(jourDepart+1)%7




voyelle=["a","e","i","o","u","y"]
def compteVoyelle(chaine):
    compteur = 0
    for n in range(len(voyelle)):
        compteur=compteur+chaine.count(voyelle[n])
    return compteur



chaine="Je m'appelle Pedro"
print(compteVoyelle(chaine))


def insertion(chaine):
    nouveauMot=""
    for v in range(len(chaine)-1):
        nouveauMot+=chaine[v]+"*"
    nouveauMot+=chaine[-1]
    return nouveauMot


print(insertion(chaine))

def inversionMot(chaine):
    nouveauMot=""
    for a in range(len(chaine)-1,-1,-1):
        nouveauMot+= chaine[a]
    return nouveauMot

mot="Pedro"
print(inversionMot(mot))

