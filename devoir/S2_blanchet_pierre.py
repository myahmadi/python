
tableOrigine=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tableCodee=  ['@','8','[','0','3','{','6','#','1','}',':','7','W','Z','*','?','O','%','$','-','V','^','M','+','/','N']


def codage(phraseClair):
    phraseClair=phraseClair.upper()
    phraseCodee=""
    for i in range(len(phraseClair)):
        for c in range(len(tableOrigine)):
            if phraseClair[i]==tableOrigine[c]:
                phraseCodee+=tableCodee[c]
        if phraseClair[i].isalpha()==False:
            phraseCodee+=phraseClair[i]

    return phraseCodee
    #A compléter

def decodage(phraseCodee):
    phraseCodee=phraseCodee.upper()
    phraseClair=""
    for i in range(len(phraseCodee)):
        for c in range(len(tableCodee)):
            if phraseCodee[i]==tableCodee[c]:
                phraseClair+=tableOrigine[c]
    return phraseClair


menu=''
while menu!='q':
    print("------------------------------------------------------------")
    print("1 : Codage d'une phrase")
    print("2 : Décodage d'une phrase")
    print("q : quitter")
    print("------------------------------------------------------------")
    menu=input("votre choix ?")
    if menu=="1":
        phrase=input("votre phrase en clair ?")
        print("La phrase codee est", codage(phrase))
    elif menu=="2":
        phrase=input("votre phrase codee ?")
        print("La phrase en clair est", decodage(phrase))


#ex 4.2
def distance_hamming(mot1, mot2):
    position1=0
    position2=0
    compteurMot1=0
    compteurMot2=0
    compteur=0
    for a in range(len(mot1)):
        compteurMot1+=1
    for b in range(len(mot2)):
        compteurMot2+=1

    if compteurMot1==compteurMot2:
        for i in range(0,len(mot1)):
            if mot1[i]!=mot2[i]:
                if compteur==1:
                    position2=i
                else:
                    compteur+=1
                    position1=i
        distance=position2-position1


    else:
        print("Les mots ne sont pas de la meme longueur")
    return distance


result=distance_hamming('lapin','satin')
print(result)


