

# Objectif Sprint 3 — US-UI-001 : IHM minimale

## Contexte
Je viens de livrer et pousser **US-002 (lancer différents dés D&D)**.  
Je démarre maintenant une **IHM douce** pour rendre le produit plus utilisable et commencer à travailler “front + back” proprement.

## Objectif du sprint
Livrer une **interface graphique minimale** (Tkinter) permettant :
- de sélectionner un type de dé (d4, d6, d8, d10, d12, d20, d100)
- de cliquer sur “Lancer”
- d’afficher le résultat en clair

## Définition de Done (DoD)
- L’IHM se lance sans erreur (commande documentée).
- Le choix du dé est possible via une liste (pas de saisie libre).
- Le bouton “Lancer” déclenche un jet en appelant la logique existante (US-002).
- Le résultat s’affiche dans l’interface.
- Le code est séparé (UI ≠ logique métier).
- Les documents du sprint sont remplis (backlog / tâches / review-rétro).
- Un commit clair est réalisé et push.

## Hors périmètre (volontaire)
- Animation du dé (style BG3)
- Historique des jets dans l’IHM
- Avantage / désavantage
- Modificateurs
- Base de données
