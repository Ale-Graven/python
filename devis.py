# -*-coding:utf-8 -*
######---------------------------------- A COMPILER SUR VISUAL STUDIO CODE DE PREFERENCE -------------------------------
#vendeur souhaitant faire un devis pour son client

#class definissant les caracteristiques des articles dont on a besoin de faire le devis ici libellé et quantité
class achat:
    def __init__(self):
        self.libelles=""
        self.quantite=int()
#suposons que le vendeur dispose de quelques articles en quantité en limitée lol
#d'ou le tableau " mini_bdd_articles " contenant tout ses articles
mini_bdd_articles=[
    ["livre",2000],
    ["ram",3000],
    ["classeur",1000],
    ["sac",2500],
    ["bic",100],
    ["cahier",500],
    ["crayon",50],
    ["regle",150],
    ["gomme",250],
    ["craie",2000],
    ["couverture",150],
    ["ensemble_geo",1500],
    ["chiffon",100]]
# odjet contenant la class achat
achater=achat()
#fonction permettant a l'utilisateur de saisir le nom et la quantité de l'article et qui retourne une liste
    

#menu principal
def menu():
    print("\n\n\t\t*********************** BIENVENU AU MAGASIN ********************\n\n")
    print("Vous etes dans l'option faire un devis\n")
    print("Pour faire un devis veuillez svp: \n")
#sous menu
def menu1():
    print("Voulez vous ajouter un autre arcticle a la liste de devis ?")
    print("1: Oui")
    print("2: Non")
    choix=int(input())
    return choix


#def retire_element_incorrect():
    #m=0
    #for itemss in mini_bdd_articles:
        #for elements in tab:
            #if elements[0]!=itemss[0]:
                #m+=1
    #if m==len(mini_bdd_articles):
        #tab.remove(elements)


tab=[]
menu()
c=True
while c:
    tabAchat=[]
    tabIncorect=[]
    p=0
    k=True
    achater.libelles=input("\nEntrez le libelles de l'article souhaiter\t")
    for nom_art in mini_bdd_articles:
        if achater.libelles!=nom_art[0]:
           p+=1
        if nom_art[0]==achater.libelles:
            tabAchat.append(nom_art[1])
    while k:
        if p==len(mini_bdd_articles):
            tabIncorect.append(achater.libelles)
            print("\nDESOLE NOUS NE DISPOSONS PAS DE CET ARTICLE !!!\n")
        k=False
    if p!=len(mini_bdd_articles):
        tabAchat.append(achater.libelles)
        achater.quantite=input("Entrez la quantite souhaiter pour l'article\t")
        tabAchat.append(achater.quantite)
    choisir=menu1()
    if choisir==1:
        tab.append(tabAchat)
        c=c
    elif choisir==2:
        c=not c
for itemers in tab:
    if not itemers:
        tab.remove(itemers)
total=0
sous_total=0
print("\n\n\t\t________________________________Liste de devis_________________________________\n")
for nom_art in tab:
    sous_total=nom_art[0]*nom_art[2]
    total+=sous_total
    print("\t\t"+nom_art[1]+"\t---->\t Quantité : {}\t Prix unitaire: {} fcfa\tTotal {} fcfa\n\n".format(nom_art[2],nom_art[0],sous_total))
print("\t\tTOTAL\t----------------------------------------------->\t {} fcfa".format(total))

################################################
    