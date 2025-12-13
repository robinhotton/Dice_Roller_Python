

# Journal des tâches — Sprint 3 (US-UI-001 : IHM minimale)

> Je garde ce journal simple : je note ce que je fais, dans l’ordre, pour montrer la progression.

## Tâches (To Do → Doing → Done)

### T1 — Préparer l’emplacement de l’IHM
- [ ] Je choisis où mettre le code UI (ex : `src/v2-gui/`).
- [ ] Je crée le fichier `app_tk.py` (ou équivalent).
- [ ] Je vérifie que je peux importer la logique de lancer sans exécuter la console.

### T2 — Créer la fenêtre Tkinter
- [ ] Je crée une fenêtre (titre + taille).
- [ ] J’ajoute un texte “Dice Roller”.

### T3 — Ajouter la sélection de dé (liste)
- [ ] Je crée une liste déroulante (dropdown) avec : 4,6,8,10,12,20,100.
- [ ] Je mets une valeur par défaut (ex : d20).

### T4 — Ajouter le bouton “Lancer”
- [ ] Je crée un bouton.
- [ ] Au clic, j’appelle la logique existante pour lancer le dé sélectionné.

### T5 — Afficher le résultat
- [ ] Je crée une zone d’affichage (Label) “Résultat : …”.
- [ ] Je mets à jour le label au clic.

### T6 — Gestion d’erreurs minimale
- [ ] Si import ou exécution échoue, j’affiche un message dans l’UI (au lieu de crash silencieux).

### T7 — Documentation de lancement
- [ ] J’ajoute une note dans le repo (README ou doc sprint) :
  - commande pour lancer l’IHM
  - prérequis (python installé)

### T8 — Commit & push
- [ ] `git status`
- [ ] `git add .`
- [ ] commit message (proposé ci-dessous)
- [ ] `git push`

---

## Message de commit proposé
- `feat: US-UI-001 IHM Tkinter minimale (sélection dé + lancer + résultat)`
