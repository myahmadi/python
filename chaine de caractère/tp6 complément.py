# Créé par PIERRE.BLANCHET, le 06/12/2022 en Python 3.7
"""
#ex1
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for i in range(len(texte)):
        texteBraille+=brailles[ord(texte[i])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))

#ex2

def insertionTexte(texte):
    inverTexte =""
    for i in range(len(texte)):
        inverTexte += texte[i]+"*"
    return inverTexte

texte=input("Mot?")
print(insertionTexte(texte))

#ex3

def inversionMot(texte):
    inverMot =""
    for i in range(1,len(texte)+1):
        inverMot += texte[-i]
    return inverMot

texte=input("Mot?")
print(inversionMot(texte))

#ex4

def palindrome(texte):
    palinMot =""
    for i in range(1,len(texte)+1):
        palinMot += texte[-i]

    return palinMot==texte


texte=input("Mot?")
print(palindrome(texte))
"""
#ex5
def codage(phraseClair,cle):
    phraseClair=phraseClair.upper()
    phraseCodee=""

    for i in range(len(phraseClair)):
        if phraseClair[i]==phraseClair.isalpha:
            ascii=ord(phraseClair[i])
            phraseClair[i]=ascii-65
            phraseClair[i]=(phraseClair[i]+cle)%26
            ascii=lettre + 65
            nouveauCaractere=chr(ascii)
            phraseCodee += nouveauCaractere
        else:
            phraseCodee += phraseClair[i]
        return phraseCodee





cle = int(input("Votre clé"))
menu=""
while menu!="q":
    print("--------------------------------")
    print("1 : Codage d'une phrase")
    print("2 : Décodage d'une phrase")
    print("3 : Changement de la clé")
    print("q : quitter")
    print("--------------------------------")
    menu=input("votre choix?")
    if menu=="1":
        phrase=input("Phrase à coder ?")
        print(codage(phrase, cle))