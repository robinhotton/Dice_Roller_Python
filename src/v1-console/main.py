# src/main.py

"""
US-002 : Lancer différents dés (d4, d6, d8, d10, d12, d20, d100)
Étape A : je demande à l'utilisateur le nombre de faces (NBR_FACES), puis je lance le dé.
"""

import random

DES_AUTORISES = [4, 6, 8, 10, 12, 20, 100]  # liste des dés autorisés. 


def roll_die(nb_faces: int) -> int: # -> int signifie que la fonction retourne un entier.
    """
    Je lance un dé à nb_faces faces.
    random.randint(1, nb_faces) inclut 1 ET nb_faces.
    """
    return random.randint(1, nb_faces) # je retourne le résultat du lancer de dé.


def main(): # point d'entrée de l'application.
    print("=== Dice Roller - US-002 : lancer un dé D&D ===") # Titre de l'application.
    print(f"Dés autorisés : {DES_AUTORISES}") # Affichage des dés autorisés.

    # Je demande le nombre de faces à l'utilisateur.
    saisie = input("Nombre de faces du dé (ex: 6 pour d6) : ") # input() retourne toujours une chaîne de caractères.

    # Je convertis la saisie en entier.
    # Si l'utilisateur tape n'importe quoi (ex: 'abc'), ça plantera : on gérera ça à l'étape suivante.
    NBR_FACES = int(saisie) # conversion de la chaîne en entier.

    # Je vérifie que le dé est autorisé.
    if NBR_FACES not in DES_AUTORISES:
        print("Dé non supporté. Choisis uniquement parmi :", DES_AUTORISES)
        return # je quitte la fonction main() prématurément.

    # Je lance le dé
    resultat = roll_die(NBR_FACES)

    # J'affiche le résultat
    print(f"Résultat du lancer (d{NBR_FACES}) : {resultat}")


if __name__ == "__main__": # point d'entrée du script.
    
    main()
