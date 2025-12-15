import random  


class DiceRoller: # classe pour gérer le lancer de dés
    DES_AUTORISES = [4, 6, 8, 10, 12, 20, 100] # liste des dés autorisés

    def roll_die(self, nb_faces: int) -> int: # méthode pour lancer un dé
        if nb_faces not in self.DES_AUTORISES:
            raise ValueError(f"Dé non supporté : d{nb_faces}")

        return random.randint(1, nb_faces)


def main(): # fonction principale
    
    print("=== Dice Roller - US-002 (OOP) ===") # titre de l'application
    roller = DiceRoller() # création d'une instance de DiceRoller

    print(f"Dés autorisés : {roller.DES_AUTORISES}") # afficher les dés autorisés
    saisie = input("Nombre de faces du dé (ex: 6 pour d6) : ") # demander le nombre de faces

    try: # conversion en entier
        nb_faces = int(saisie) # conversion de la saisie en entier

    except ValueError: # gestion d'erreur
        print("Entrée invalide : merci de saisir un entier (ex: 6).")
        return

    if nb_faces not in roller.DES_AUTORISES: # validation du dé
        print("Dé non supporté. Choisis uniquement parmi :", roller.DES_AUTORISES)
        return  
    
    else: # lancer le dé
        try: # lancer le dé avec gestion d'erreur
            resultat = roller.roll_die(nb_faces)

        except ValueError as e: # gestion d'erreur
            print(e)
            return # sortir de la fonction main
        print(f"Résultat du lancer (d{nb_faces}) : {resultat}") # afficher le résultat


if __name__ == "__main__":
    main()
