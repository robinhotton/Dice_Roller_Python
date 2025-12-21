# src/v2-gui/app_tk.py


# US-UI-001 : IHM minimale (Tkinter) - orientée objet
# Objectif : sélectionner un dé (d4..d100), cliquer "Lancer", afficher le résultat.


import tkinter as tk
from tkinter import ttk

# J'importe la logique métier existante (le moteur).
# Si ta classe / fichier n'a pas exactement ce nom, tu ajusteras cette ligne.

from src.v1_console.dice_roller import DiceRoller


class DiceRollerApp(tk.Tk): # hérite de tk.Tk
    
    # Application Tkinter orientée objet.
    # Ici je garde l'UI séparée de la logique : l'UI appelle DiceRoller, point.
    

    DES_AUTORISES = [4, 6, 8, 10, 12, 20, 100] # liste des dés autorisés (source de vérité).

    def __init__(self): # constructeur de la classe
        super().__init__()

        # --- Configuration de la fenêtre ---
        self.title("Dice Roller - IHM minimale")
        self.geometry("420x220")
        self.resizable(False, False)

        # --- Moteur de lancer de dés ---
        self.roller = DiceRoller()

        # --- Variables Tkinter (état de l'app) ---
        self.nb_faces_var = tk.StringVar(value="20")  # par défaut d20
        self.result_var = tk.StringVar(value="Résultat : -")

        # --- Construction de l'interface ---
        self._build_ui()

    def _build_ui(self): #    
        #Je construis les widgets de l'interface (labels, dropdown, bouton).

        root = ttk.Frame(self, padding=16)
        root.pack(fill="both", expand=True)

        titre = ttk.Label(root, text="Dice Roller", font=("Segoe UI", 16, "bold"))
        titre.pack(anchor="w")

        sous_titre = ttk.Label(
            root,
            text="Sélectionne un dé, puis clique sur “Lancer”.",
        )
        sous_titre.pack(anchor="w", pady=(4, 16))

        # Ligne : sélection du dé
        ligne_de = ttk.Frame(root)
        ligne_de.pack(fill="x", pady=(0, 12))

        label_de = ttk.Label(ligne_de, text="Type de dé :")
        label_de.pack(side="left")

        self.combo_de = ttk.Combobox(
            ligne_de,
            textvariable=self.nb_faces_var,
            values=[str(x) for x in self.DES_AUTORISES],
            state="readonly",
            width=8
        )
        self.combo_de.pack(side="left", padx=(10, 0))
        self.combo_de.set("20")

        # Bouton lancer
        bouton = ttk.Button(root, text="Lancer", command=self.on_roll_click)
        bouton.pack(anchor="w", pady=(0, 12))

        # Résultat
        resultat_label = ttk.Label(root, textvariable=self.result_var, font=("Segoe UI", 12))
        resultat_label.pack(anchor="w")

    def on_roll_click(self):
        # Action déclenchée quand je clique sur 'Lancer'.

        # Je récupère le nombre de faces sélectionné dans le dropdown
        try:
            nb_faces = int(self.nb_faces_var.get())
        except ValueError:
            self.result_var.set("Résultat : entrée invalide")
            return

        # Je sécurise : uniquement les dés autorisés
        if nb_faces not in self.DES_AUTORISES:
            self.result_var.set("Résultat : dé non supporté")
            return

        # J'appelle le moteur (logique métier)
        try:
            resultat = self.roller.roll_die(nb_faces)
            # resultat = 1 # pour tester l'échec critique
            # resultat = 20 # pour tester le critique 
        except Exception:
            # Je ne détaille pas l'erreur côté UI, je garde un message simple.
            self.result_var.set("Résultat : erreur au lancer")
            return

        if resultat == 20 and nb_faces == 20 :                                      # critique réussi 
            self.result_var.set(f"🎉 {resultat} c'est une Reussite Critique ! 🎉")
        elif resultat == 1 and nb_faces == 20 :                                     # échec critique 
            self.result_var.set(f" Tu as fait {resultat} \n c'est un 💀 Échec critique ! 💀")

        else:
            #print(f"Résultat du lancer (d{nb_faces}) : {resultat}") # afficher le résultat
            self.result_var.set(f"Résultat du lancer (d{nb_faces} → {resultat})")


if __name__ == "__main__":
    app = DiceRollerApp()
    app.mainloop()
