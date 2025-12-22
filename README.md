# 🎲 Dice Roller Python — D&D (Tkinter)

Un programme Python pour lancer des dés **Dungeons & Dragons** depuis ton PC, avec une **IHM Tkinter** et une logique métier séparée (core).  
Ce projet sert aussi de **support de reconversion professionnelle** : je l’utilise comme vitrine d’apprentissage (code, Git, documentation, incréments).  
👉 Profil LinkedIn : https://www.linkedin.com/in/xavierdeguercy/

---

## 🎯 Contexte du projet (reconversion + apprentissage)

- **Objectif** : construire un petit produit utile, évolutif et propre (comme un vrai projet)  
- **Pourquoi ce projet** :
  - je joue à D&D en ligne et j’ai besoin de “roll the dice” rapidement
  - je veux une expérience plus immersive à terme (inspiration **Baldur’s Gate 3** : animation du dé)
- **Cadre pédagogique** :
  - projet “sideboard” / fil rouge pour appliquer ce que j’apprends en **développement Python orienté objet**
  - pratique de Git/GitHub, structuration, documentation et méthode Scrum

---

## ✅ Fonctionnalités

### Dés supportés
- d4, d6, d8, d10, d12, d20  
- d100 (simulé via **2d10** : dizaines + unités)

### Règles D&D incluses
- **Critiques d20**
  - 1 = échec critique
  - 20 = réussite critique
- **Avantage / Désavantage (d20 uniquement)**
  - avantage : 2d20, garder le meilleur
  - désavantage : 2d20, garder le moins bon
- **Inspiration bardique (+1d4)** (option dans l’IHM)

### Multi-dés (US-003)
- Lancer **N dés** du même type (ex. `3d6`, `4d10`, etc.)
- Affichage : **résultats individuels + total**

---

## 🖥️ Lancer l’application (IHM)

> Depuis la racine du dépôt :

```bash
python -m src.v2_gui.app_tk
