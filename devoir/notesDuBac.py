#import pygal   #question 8

coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]


def calculMoyenne(coefficients,notes):
    somme=0
    for i in range(len(notes)):
        somme=somme+notes[i]*coefficients[i]
    moyenne=somme/100

    return moyenne


def traitementBac(moyenne):
    print ("Votre moyenne est de",moyenne)
    if moyenne<8.0:
        print("Vous n'avez pas le BAC, désolé")
    elif moyenne >= 8.0 and moyenne < 10.0:
        print("Vous devez aller au rattrapage")
    elif moyenne >= 10.0 and moyenne < 12.0:
        print("Vous avez le BAC")
    elif moyenne >= 12.0 and moyenne < 14.0:
        print("Vous avez le BAC avec mention assez bien")
    elif moyenne >= 14.0 and moyenne < 16.0:
        print("Vous avez le BAC avec mention bien")
    else:
        print("Vous avez le BAC avec mention très bien")
    #a completer question 2


def rechercheNoteMin(notes):
    min=notes[0]
    for i in range(1,len(notes)):
        if notes[i] < min:
            min=notes[i]
    return min

    # a completer question 3


def rechercheNoteMax(notes):
    max=notes[0]
    for i in range(1,len(notes)):
        if notes[i] > max:
            max=notes[i]
    return max

    # a completer question 4

def rechercheNote(notes,matieres,laNote):
    compteur=0
    for i in range(len(notes)):
        if notes[i]==laNote:
            print("Vous avez obtenu ", laNote," dans la matière", matieres[i])
            compteur+=1
    print("Vous avez obtenu", laNote," dans ", compteur," matière(s)")
    # a completer question 5

def changeNote(notes):
    somme=0
    for i in range(len(notes)):
        nouvelleNote=25.0
        while nouvelleNote > 20.0 or nouvelleNote<0.0:
            print("Quel est votre note en", matieres[i])
            nouvelleNote=float(input())
        notes[i]= nouvelleNote
        somme+=notes[i]
        moyenne=somme/len(notes)


    print(notes)
    print(moyenne)
    print("La note minimale est de ", rechercheNoteMin(notes),"/ 20")
    print("La note maximale est de ", rechercheNoteMax(notes),"/ 20")



    #a completer question 6
    pass


def tableauBac(coefficients,notes,matieres):
    #a completer question 7
    for n in range(len(notes)):
        print("{0:35} {1:5} {2:7}".format(matieres[n],coefficients[n],notes[n]))
    pass


#changeNote(notes)
moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
print("La note minimale est de ", rechercheNoteMin(notes),"/ 20")
print("La note maximale est de ", rechercheNoteMax(notes),"/ 20")


rechercheNote(notes,matieres,12)
#changeNote(notes)
tableauBac(coefficients,notes,matieres)

#line_chart = pygal.HorizontalBar()
#line_chart.title = 'Notes du Bac (/20)'
#a completer question 8

#line_chart.render_to_file('notes.svg')

