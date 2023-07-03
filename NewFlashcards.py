# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:12:40 2019

@author: Simon Biffe
"""
from BiblioFonctions import ImportationSauvegarde, ExportationSauvegarde, AjoutFlashcard, TirageFlashcard, VoirListe
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

nomsDesListes = ImportationSauvegarde("Listes.li", "\n", 1)
listesDeMotsARetenir = {}
for i in range (0, len(nomsDesListes)):
    listesDeMotsARetenir[nomsDesListes[i]] = ImportationSauvegarde(f"{nomsDesListes[i]}.li", "\n", 2)
        
def main(nomsDesListes, listesDeMotsARetenir) :
    choix = int(input ("Tapez 1 pour ajouter quelque chose à retenir. \nTapez 2 pour tirer une donnée au hasard. \nTapez 3 pour voir les flashcards enregistrées. \nTapez 4 pour quitter le programme. \n"))
    if choix == 1 :
        print('Choisissez un liste parmi celles-ci ou tapez "Nouvelle" pour créer une nouvelle liste')
        for i in range (1, len(nomsDesListes)):
            print(nomsDesListes[i], end="  ")
        listeChoisie = input("\n")
        if listeChoisie == "Nouvelle" or listeChoisie in nomsDesListes:
            if listeChoisie == "Nouvelle":
                nouvelleListe = input("Entrez le nom de la nouvelle liste :")
                nomsDesListes.append(nouvelleListe)
                listeChoisie = nouvelleListe
                listeAExporter = nomsDesListes[:]
                ExportationSauvegarde(listeAExporter, "Listes.li", "\n")
                listesDeMotsARetenir[nouvelleListe] = []
                AjoutFlashcard(listesDeMotsARetenir["Toutes"], listesDeMotsARetenir[nouvelleListe], nouvelleListe)
            else:
                AjoutFlashcard(listesDeMotsARetenir["Toutes"], listesDeMotsARetenir[listeChoisie], listeChoisie)
            rejouer = input("Tapez s pour revenir à la liste des choix ou entrez un autre caractère pour ajouter à nouveau une flashcard dans cette liste.")
            while rejouer != "s":
                AjoutFlashcard(listesDeMotsARetenir["Toutes"], listesDeMotsARetenir[listeChoisie], listeChoisie)
                rejouer = input("Tapez s pour revenir à la liste des choix ou entrez un autre caractère pour ajouter à nouveau une flashcard dans cette liste.")
        else:
            print("Choix impossible !")
        main(nomsDesListes, listesDeMotsARetenir)
    elif choix == 2 :
        print("Parmi quelle liste voulez-vous tirer une flashcard ?")
        for i in range (0, len(nomsDesListes)):
            print(nomsDesListes[i], end="  ")
        listeChoisie = input("\n")
        if listeChoisie in nomsDesListes:
            TirageFlashcard(listesDeMotsARetenir[listeChoisie])
            rejouer = input("Tapez s pour revenir à la liste des choix ou entrez un autre caractère pour tirer à nouveau une flashcard dans cette liste.")
            while rejouer != "s":
                TirageFlashcard(listesDeMotsARetenir[listeChoisie])
                rejouer = input("Tapez s pour revenir à la liste des choix ou entrez un autre caractère pour tirer à nouveau une flashcard dans cette liste.")
        else:
            print("Liste inexistante !")
        main(nomsDesListes, listesDeMotsARetenir)
    elif choix == 3 :
        print("Quelle liste voulez-vous voir ?")
        for i in range (0, len(nomsDesListes)):
            print(nomsDesListes[i], end="  ")
        listeChoisie = input("\n")
        if listeChoisie in nomsDesListes:
            VoirListe(listesDeMotsARetenir[listeChoisie])
        else:
            print("Liste inexistante !")
        main(nomsDesListes, listesDeMotsARetenir)
    elif choix == 4 :
        print ("Au revoir !")
    else :
        print ("Ceci n'est pas une option !")
        main(nomsDesListes, listesDeMotsARetenir)

main(nomsDesListes, listesDeMotsARetenir)