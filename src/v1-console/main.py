# src/main.py

"""
Étape 1 : premier lancer de dé
- Objectif : afficher le résultat d'un lancer de dé à 6 faces.
"""

# 1. Importer le module random de la bibliothèque standard
import random


def main():
    """
    Point d'entrée du programme.
    Pour l'instant :
    - on lance un seul dé à 6 faces
    - on affiche le résultat
    """

    print("=== Dice Roller - Étape 1 : un seul dé à 6 faces ===")

    # 2. Générer un nombre aléatoire entre 1 et 6 (inclus)
    # random.randint(a, b) renvoie un entier entre a et b, bornes incluses.
    resultat = random.randint(1, 6)

    # 3. Afficher le résultat
    print(f"Résultat du lancer : {resultat}")


# 4. Ce bloc permet de lancer main() seulement si le fichier est exécuté directement
if __name__ == "__main__":
    main()
