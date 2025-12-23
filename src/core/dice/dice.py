import random

class Dice:
    """Représente un dé physique simple"""
    
    def __init__(self, faces: int):
        self.faces = faces
    
    def roll(self) -> int:
        """Lance le dé et retourne le résultat"""
        return random.randint(1, self.faces)
    
    def roll_multiple(self, count: int) -> list[int]:
        """Lance le dé plusieurs fois"""
        return [self.roll() for _ in range(count)]