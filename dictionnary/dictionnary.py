# Créé par PIERRE.BLANCHET, le 02/02/2023 en Python 3.7
"""
stock={'poires':5,'pommes':10,'fraises':35}
print(len(stock))
print(stock['fraises'])

stock={'poires':5,'pommes':10,'fraises':35}
inventaire=""
for nom in stock.keys():
    inventaire += nom + ', '
print(inventaire)


stock={'poires':5,'pommes':10,'fraises':35}
for num in stock.values():
    print (num)


stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

for nom, num in stock.items():
    print(nom, '->',num)



stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print('fraises' in stock.keys())
print('banane' in stock.keys())
print(7 in stock.values())
print(5 in stock.values())
print(3 in stock.values())


stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
stock["fraises"]=20
print(stock)
stock["abricots"]=15
print(stock)


stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
del stock["fraises"]
print(stock)
valeur = stock.pop("pommes")
print(stock)
print(valeur)



d = { 'Croissants':6 , 'Pizza':2, 'Café en grains':3, "Riz":1}


def occurences(chaine1, chaine2):
    D = {}
    L = {}
    for caractere in chaine1:
        if caractere in D:
            D[caractere]+=1
        else:
            D[caractere]=1
    for caractere in chaine2:
        if caractere in L:
            L[caractere]+=1
        else:
            L[caractere]=1
    del D[" "]
    del L[" "]
    if D==L:
        return True
    else:
        return False
print(occurences('le rechauffement climatique', 'ce fuel qui tache le firmament'))

pieces=[500,200,100,50,20,10,5,2,1]
somme=780

def renduMonnaie(somme,pieces):
    choisie={}
    for p in pieces:
        nb= somme//p
        choisie[p]=nb
        somme+=-nb*p
    return choisie
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
"""
