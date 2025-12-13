

# Sprint Review & Rétrospective — Sprint 3 (US-UI-001 : IHM minimale)

## Sprint Review

### Objectif du sprint
Livrer une IHM Tkinter minimale permettant de sélectionner un dé et d’afficher un résultat.

### Ce qui a été livré
- [ ] IHM Tkinter minimale :
  - sélection du dé (d4, d6, d8, d10, d12, d20, d100)
  - bouton “Lancer”
  - affichage du résultat
- [ ] Réutilisation de la logique existante (US-002)
- [ ] Documentation de lancement
- [ ] Commit + push

### Démonstration (scénario)
1. Je lance l’application (commande documentée).
2. Je sélectionne d20.
3. Je clique “Lancer”.
4. Je vois “Résultat : X” (entre 1 et 20).
5. Je refais la même chose avec d100.

### Écarts / Non fait
- [ ] (à remplir si besoin)

### Liens
- Dépôt : https://github.com/xavier-deguercy/Dice_Roller_Python
- Commit / branche : **[À renseigner]**

---

## Rétrospective

### Ce qui a bien fonctionné
- [ ] Découpage clair (UI séparée de la logique métier).
- [ ] Incrément visible rapidement.
- [ ] Réutilisation du code existant.

### Ce qui a été difficile
- [ ] (ex : imports / chemins / organisation de fichiers)

### Ce que je peux améliorer au prochain sprint
- [ ] Clarifier les points d’entrée (console vs GUI).
- [ ] Ajouter une petite structure UI (ex : dossier `ui/` dédié si besoin).
- [ ] Préparer l’historique ou l’avantage/désavantage en US séparées.

### Actions concrètes (Next sprint)
- [ ] Proposer US-006 : avantage/désavantage (2d20)
- [ ] Proposer US-007 : modificateur (+X)
- [ ] Proposer US-UI-002 : historique des jets dans l’IHM
