# src/main.py

"""
US-002 : Dice Roller en orienté objet (OOP)
Étape B : je crée une classe DiceRoller qui sait lancer un dé.


"""

import random  # Générateur pseudo-aléatoire standard de Python (randint, etc.)


class DiceRoller:
    # Liste centralisée des dés autorisés (source de vérité).
    DES_AUTORISES = [4, 6, 8, 10, 12, 20, 100]

    def roll_die(self, nb_faces: int) -> int: # Méthode pour lancer un dé à nb_faces faces.
        """
        Je lance un dé à nb_faces faces.
        random.randint(1, nb_faces) inclut 1 ET nb_faces.
        """
        # Je sécurise la méthode : même si elle est appelée ailleurs, elle reste fiable.
        if nb_faces not in self.DES_AUTORISES:
            raise ValueError(f"Dé non supporté : d{nb_faces}")

        return random.randint(1, nb_faces)


def main(): # Point d'entrée principal du programme.
    print("=== Dice Roller - US-002 (OOP) ===")

    # Je crée une instance du "service" de lancer de dés.
    roller = DiceRoller()

    # J'affiche la liste des dés disponibles pour guider l'utilisateur.
    print(f"Dés autorisés : {roller.DES_AUTORISES}")

    # Je récupère la saisie utilisateur (toujours une chaîne via input()).
    saisie = input("Nombre de faces du dé (ex: 6 pour d6) : ")

    try:
        nb_faces = int(saisie)
    except ValueError:
        print("Entrée invalide : merci de saisir un entier (ex: 6).")
        return

    # Je garde la validation côté main() pour expliquer clairement à l'utilisateur ce qui est attendu.
    if nb_faces not in roller.DES_AUTORISES:
        print("Dé non supporté. Choisis uniquement parmi :", roller.DES_AUTORISES)
        return  # je quitte la fonction main() prématurément.
    else:
        # Peut être retiré (le return suffit), mais je le garde pour le côté pédagogique.
        # Je garde aussi un try/except : la classe protège roll_die() si elle est appelée ailleurs.
        try:
            resultat = roller.roll_die(nb_faces)
        except ValueError as e:
            print(e)
            return

        # J'affiche le résultat
        print(f"Résultat du lancer (d{nb_faces}) : {resultat}")


if __name__ == "__main__":
    main()
