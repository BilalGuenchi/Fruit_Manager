# # Inventaire de fruits

import json

def ouvrir_inventaire(path='inventaire.json'):
    with open(path, 'r', encoding='utf-8') as f:
        inventaire = json.load(f)
    return inventaire

def ecrire_inventaire(inventaire, path='inventaire.json'):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(f, path, ensure_ascii=False, indent=4)

inventaire = ouvrir_inventaire('data/inventaire.json')

def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")

afficher_inventaire(inventaire)

def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"Récolté {quantite} {fruit} supplémentaires")

recolter(inventaire, "bananes", 10)

afficher_inventaire(inventaire)

def vendre(inventaire, fruit, quantite):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        print(f"Vendu {quantite} {fruit}")
    else:
        print("Pas assez de {fruit} pour vendre {quantite} unités")

vendre(inventaire, "bananes", 5)

afficher_inventaire(inventaire)