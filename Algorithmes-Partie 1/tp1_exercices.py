"""
#ex1

a = 4
carre = a**2
print("la valeur de a = ",a,"au carré est de ", carre)

#ex2

kilometre = 100
miles = kilometre/1.609

print("La distance de ",kilometre,"kilomètre est de ", miles," miles")

#ex3

a = 2
b = 3

print("Avant l'échange a = ",a, "et b = ",b)
temp = a
a=b
b=temp

print("Après échange a = ",a," et b = ",b)

#ex4

valeur_tva = 20

prix_ht = 40
tva = prix_ht*valeur_tva/100
prix_ttc = prix_ht+tva

print("Prix HT du produit : ",prix_ht," C")
print("Indice de la TVA en 2015 : ",valeur_tva," %")
print("Valeur de la TVA : ",tva," €")
print("Prix TTC : ",prix_ttc, " €")


#ex5

a=3
b=15
r=a*b

if r > 0:
    print("Le produit est positif")
elif r < 0:
    print("Le produit est négatif")
else:
    print("Ton produit est égale a 0")

#ex6

age = 14
if age >= 6 & age <= 7:
    print("Poussin")
elif age >= 8 & age <= 9:
    print("Pupille")
elif age >= 10 & age <= 11:
    print("Minime")
elif age >= 12 & age <= 15:
    print("Cadet")
else:
    print("Hors catégorie")

#ex7

nb_valeur = 10
result = 0
temp = 0

for i in range(0,nb_valeur):
    temp = temp + 1
    result = temp + result

print("Somme des ",nb_valeur," premiers nombres entiers est : ", result)


#ex8
table = 0

for i in range(0,11):
    table2 = 0
    for j in range(0,11):
        print(table * table2, end=" ")
        table2 = table2 + 1
    table = table + 1
    print()


"""

