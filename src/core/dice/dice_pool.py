from .dice import Dice

class DicePool:
    """Gère un ensemble de dés à lancer
    Exemple: 1d6 + 2d8"""
    
    def __init__(self):
        self._dice: list[Dice] = []
    
    def add_die(self, faces: int, count: int = 1):
        """Ajoute des dés au pool"""
        for _ in range(count):
            self._dice.append(Dice(faces))
        return self

    def roll_all(self) -> list[int]:
        """Lance tous les dés du pool"""
        return [die.roll() for die in self._dice]
    
    def clear(self):
        """Vide le pool"""
        self._dice.clear()
