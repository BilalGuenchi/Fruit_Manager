# # Inventaire de fruits

import json

def ouvrir_inventaire(path='data/inventaire.json'):
    with open(path, 'r', encoding='utf-8') as f:
        inventaire = json.load(f)
    return inventaire

def ecrire_inventaire(inventaire, path='data/inventaire.json'):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(inventaire, f, ensure_ascii=False, indent=4)

def ouvrir_tresorerie(path='data/tresorerie.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        tresorerie = json.load(f)
    return tresorerie

def ecrire_tresorerie(tresorerie, path='data/tresorerie.txt'):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(tresorerie, f, ensure_ascii=False, indent=4)

def afficher_tresorerie(tresorerie):
    print(f"Tresorerie actuelle actuel : {tresorerie:.2f} $")

def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")

def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"Récolté {quantite} {fruit} supplémentaires")
    return inventaire

def vendre(inventaire, fruit, quantite, tresorerie):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += 1 * quantite
        print(f"Vendu {quantite} {fruit}")
        return (inventaire, tresorerie)
    else:
        print("Pas assez de {fruit} pour vendre {quantite} unités")


if __name__ == "__main__":
    inventaire = ouvrir_inventaire('data/inventaire.json')
    tresorerie = ouvrir_tresorerie('data/tresorerie.txt')
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)

    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie)

    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)

