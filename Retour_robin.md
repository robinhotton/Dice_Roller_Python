Salut xavier,

Comme amélioration pour ton code, vu que tu as plusieurs façons pour lancer des dés, je te conseille de regarder le design pattern [STRATEGY](https://refactoring.guru/fr/design-patterns/strategy).

Le but est de séparer la logique de chaque type de lancer dans une classe dédiée, et d'avoir une classe "contexte" qui va utiliser la stratégie choisie. Cela permet d'avoir un code plus découper entre logique et execution, pour faciliter les ajouts futurs et la maintenance.

J'ai fais une ébauche d'implémentation. Pour exécuter : `python -m src.core.dice_roller`
```
{'strategy': 'normal', 'rolls': [2], 'final_value': 2, 'die_faces': 6}
{'strategy': 'advantage', 'rolls': [11, 15], 'final_value': 15, 'die_faces': 20}
{'strategy': 'disadvantage', 'rolls': [1, 4], 'final_value': 1, 'die_faces': 10}
```

Par contre, je n'ai pas touché a tkinter.