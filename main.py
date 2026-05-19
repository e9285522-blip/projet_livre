#application de gestion de livre

livre = ["merlin","Voiture", "Arthur"]

def afficher_menu():
    print("\n==== MENU PRINCIPAL ====")
    print("1. Afficher les livres")
    print("2. Ajouter un livre")
    print("3. Modifier un livre")
    print("4. Supprimer un livre")
    print("5. Quitter")
def afficher_livres():
    for l in livre:
        print(l)
def ajouter_livre():
    nom = input("Entrez le nom du livre à ajouter: ")
    livre.append(nom)
    print(f"Le livre '{nom}' a été ajouté.")
def modifier_livre():
    nom = input("Entrez le nom du livre à modifier: ")
    if nom in livre:
        nouveau_nom = input("Entrez le nouveau nom du livre: ")
        index = livre.index(nom)
        livre[index] = nouveau_nom
def supprimer_livre():
    nom = input("Entrez le nom du livre à supprimer: ")
    if nom in livre:
        livre.remove(nom)
        print(f"Le livre '{nom}' a été supprimé.")
    else:
        print(f"Le livre '{nom}' n'existe pas.")
        