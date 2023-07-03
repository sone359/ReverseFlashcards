# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:20:35 2020

@author: Simon Biffe
"""
from random import randint

def ImportationSauvegarde (nomDeLaSauvegarde, separateur, periode):
    """
    Fonction prenant en paramètre un fichier servant de sauvegarde, une chaîne
    de caractères servant à séparer le texte stocké dans le fichier et une 
    fixant le nombre d'éléments que doit contenir chaque sous-liste.
    Si la période est de 1, elle retourne une liste contenant les éléments 
    sauvegardés. Sinon, elle retourne une liste contenant des sous-liste 
    correspondant aux éléments sauvegardés et qui contiennent elles-mêmes des 
    chaînes de caractères.
        >>> ImportationSauvegarde ("participants.txt", "\\n", 2)
        [['Luke', 'Skywalker'], ['Harry', 'Potter'], ['Pierre', 'Boterro'], ['Kvothe', 'Rothfuss']]
    """
    elementsSauvegarde = []
    with open(nomDeLaSauvegarde, "r", encoding='utf-8') as fichierSauvegarde:
        chaineSauvegarde = fichierSauvegarde.read()
        listeSauvegarde = chaineSauvegarde.split(separateur)
        if periode == 1:
            for i in range (0, len(listeSauvegarde)//periode):
                elementsSauvegarde.append(listeSauvegarde[i])
        else:
            for i in range (0, len(listeSauvegarde)//periode):
                elementsSauvegarde.append(listeSauvegarde[i*periode:(i+1)*periode])
    return elementsSauvegarde

def ExportationSauvegarde (listeASauvegarder, nomDeLaSauvegarde, separateur):
    """
    Fonction prenant en paramètre une liste composée d'éléments à sauvegarder,
    un fichier servant de sauvegarde et une chaîne de caractères servant à 
    séparer le texte stocké dans le fichier.
    Elle ne retourne rien mais la liste est sauvegardée sous forme de texte 
    dans le fichier de sauvegarde et peut-être récupérer sous forme de liste
    avec ImportationSauvegarde(nomDeLaSauvegarde, separateur, periode).
    """
    for i in range (0, len(listeASauvegarder)):
        if type(listeASauvegarder[i]) == list:
            listeASauvegarder[i] = separateur.join(listeASauvegarder[i])
    listeASauvegarder = separateur.join(listeASauvegarder)
    with open(nomDeLaSauvegarde, "w", encoding='utf-8') as fichierSauvegarde:
        fichierSauvegarde.write(listeASauvegarder)
        
def AjoutFlashcard (listeComplete, listeChoisie, nomListeChoisie):
    recto = input ("Quelle est la face recto de votre flashcards ? \n")
    verso = input ("Quelle est la face verso de votre flashcards ? \n")
    listeChoisie.append([recto, verso])
    listeChoisie.append([verso, recto])
    listeComplete.append([recto, verso])
    listeComplete.append([verso, recto])
    listeSauvee = listeChoisie[:]
    ExportationSauvegarde (listeSauvee, f"{nomListeChoisie}.li", "\n")
    listeSauvee = listeComplete[:]
    ExportationSauvegarde (listeSauvee, "Toutes.li", "\n")
    
def TirageFlashcard (listeChoisie):
    motTiré = randint(0, len(listeChoisie)-1)
    print (listeChoisie[motTiré][0])
    input ("Entrez un caractère pour voir la face verso \n")
    print (listeChoisie[motTiré][1])
    
def VoirListe (listeChoisie):
    print(listeChoisie)
    
    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#ExportationSauvegarde ([['Luke', 'Skywalker'], ['Harry', 'Potter'], ['Pierre', 'Boterro'], ['Kvothe', 'Rothfuss']], "participants.txt", "\n")