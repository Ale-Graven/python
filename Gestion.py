from random import *
from os import *
class stock:
    def __init__(self):
        self.design=str()
        self.Code=str()
        self.prixU=0
        self.quantite=0

objet=stock()
def ajouter():
    print("\n\n*****Pour ajouter un article veuillez:********\n")
    tab=[]
    objet.design=input("Entrez la designation\t")
    tab.append(objet.design)
    objet.Code=input("Entrez un code pour l'article\t")
    tab.append(objet.Code)
    objet.prixU=int(input("Entrez son prix\t"))
    tab.append(objet.prixU)
    objet.quantite=int(input("Entrez sa quantite\t"))
    tab.append(objet.quantite)
    return tab

#def modifier(listeArticle):
    #codeR=input("Veuillez entrer le code de l'article modifier !\t")
    #for i in range(0, len(listeArticle)):
        #if tabarticle[i].Code==codeR:



def suprim(cod):
    for Articles in tabarticle:
        if cod==Articles[1]:
            tabarticle.remove(Articles)
            print("Article supprime avec succes")
        else: print("Aucun article ne correspond a ce code")

def plusChere(chere):
    for Articles in tabarticle:
        if Articles[2]>chere:
            chere=Articles[2]
    print("L'article le plus chere est:\n")
    print("Designation: "+Articles[0])
    print("Code: "+Articles[1])
    print("Prix unitaire: {} fcfa".format(Articles[2]))
    print("Quantite: {}".format(Articles[3]))
    return chere

def moinChere(moin):
    for Articles in tabarticle:
        if Articles[2]<moin:
            moin=Articles[2]
    print("L'article le moins chere est:\n")
    print("Designation: "+Articles[0])
    print("Code: "+Articles[1])
    print("Prix unitaire: {} fcfa".format(Articles[2]))
    print("Quantite: {}".format(Articles[3]))
    return moin

def valeurGlobal():
    valeur_globale=0
    print("La liste du stock est:\n")
    for Articles in tabarticle:
     valeur_globale=valeur_globale+(Articles[2]*Articles[3])
     print("_________________________________________________\n")
     print("Designation: "+Articles[0])
     print("Code: "+Articles[1])
     print("Prix unitaire: {} fcfa".format(Articles[2]))
     print("Quantite: {}".format(Articles[3]))
     print("_________________________________________________\n")
    print("Le stock actuel vaut: {} fcfa".format(valeur_globale))

def menu():
    print("Tapez:\n1: Pour ajouter un article au stock\n2: Pour modiffier la quantite d'un article\n3: Pour modiffier le prix d'un article\n4: Pour supprimer un article de la liste\n5: Afficher l'article plus chere\n6: Afficher le moins chere\n7: Valeur globale du stock\n0: Quitter")
    choi=int(input())
    return choi

tabarticle=[]
c=True
while c:
    print("\n\n********* BIENVENUE DANS LE SUPER GESTIONNAIRE DE STOCK (Forum d'adjame :-) )************\n")
    choix=menu()
    if choix==1:
        tabarticle.append(ajouter())
        print("Article bien ajouter")
    elif choix==2:
       codeR=input("Entrez le code de l'article a modiffier\t")
       for Articles in tabarticle:
           if codeR==Articles[1]:
               Articles[3]=int(input("Veuillez entrer la nouvelle quantite pour l'article \t"+Articles[0]))
               print("\nQuantite modiffier avec succes:\n")
               print("Designation: "+Articles[0])
               print("Code: "+Articles[1])
               print("Prix unitaire: {} fcfa".format(Articles[2]))
               print("Quantite: {}".format(Articles[3]))
           else: 
               print("\nAucun article ne correspond a code !!!")
    elif choix==3:
        codeR=input("Entrez le code de l'article a modiffier\t")
        for Articles in tabarticle:
           if codeR==Articles[1]:
               Articles[2]=int(input("Veuillez entrer le nouveau prix unitaire pour l'article\t"))
               print("\nPrix unitaire modiffier avec succes:\n")
               print("Designation: "+Articles[0])
               print("Code: "+Articles[1])
               print("Prix unitaire: {} fcfa".format(Articles[2]))
               print("Quantite: {}".format(Articles[3]))
           else: 
               print("\nAucun article ne correspond a code !!!")
    elif choix==4:
        codeR=input("Entrez le code l'article a supprimer\t")
        suprim(codeR)
    elif choix==5:
        plus_chere=0
        plusChere(plus_chere)
    elif choix==6:
        moin_chere=0
        moinChere(moin_chere)
    elif choix==7:
        valeurGlobal()
    elif choix==0:
        print("Bye")
        c=False
    else: print("choix non disponible !")
        
#********************************************
#creat by Kla Gueu********************************************************
#********************************************
        