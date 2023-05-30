#ex 1
"""
phrase = "bonjour"
print (phrase[1:4])

chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)

w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))

chaine = "Bonjour"
for i in range(0, len(chaine)):
    print(chaine[i], end = '')

chaine = "Au revoir"
for c in chaine:
    print(c, end = '')


chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')


s = "Welcome"
print(s[-1])
print(s[-2])

s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])

s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))


chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)


ch = 'A'
print(ord(ch))


valeur=66
print(chr(valeur))

chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)

#ex2

def compteLettre(lettre,chaine):
    a=chaine.count(lettre)
    return a


print(compteLettre("e","je vais au cine ce soir"))


def compteLettre(lettre,chaine):
    total = 0
    for i in range(len(chaine)):
        if chaine[i]=="e":
            total+=1

    return total

print(compteLettre("e","je vais au cine ce soir"))

#ex3

def fonctionpremierMot(chaine):
    mot=''
    for i in range(len(chaine)):
        if chaine[i]==' ':
            return mot
        else: mot+=chaine[i]



print(fonctionpremierMot("enfin il arrête de pleuvoir "))

#ex4

text1="Un peu"
text2="Beaucoup"
text3="Passionnément"

textfinale= text1+"\r"+text2+"\r"+text3

print(textfinale)

#ex5

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in range(len(semaine)):
    print(semaine[i])

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in semaine:
    print(i)
"""
#ex6

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
j=1
for i in range(1,32):

    print(semaine[j-2],i,"décembre")
    j+=1
    if j==8:
        j=1

