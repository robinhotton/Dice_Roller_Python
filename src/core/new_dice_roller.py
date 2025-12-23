from .dice import Dice
from .validators import DiceValidator
from .strategies import RollStrategy, NormalRoll, AdvantageRoll, DisadvantageRoll

class DiceRoller:
    """
    Interface principale pour tous les types de lancers.
    Combine validation, création de dés et stratégies.
    """
    
    def __init__(self, validator: DiceValidator = None):
        self.validator = validator or DiceValidator()
    
    def roll(self, faces: int, strategy: RollStrategy = None) -> dict:
        """
        Lance un dé avec une stratégie donnée.
        
        Args:
            faces: Nombre de faces du dé
            strategy: Stratégie de lancer (None = normal)
        
        Returns:
            Dictionnaire avec les détails du lancer
        """
        self.validator.validate_die(faces)
        
        die = Dice(faces)
        strategy = strategy or NormalRoll()
        result = strategy.execute(die)
        
        # Ajoute les infos du dé
        result["die_faces"] = faces
        return result
    
    # Méthodes de commodité
    def roll_normal(self, faces: int) -> dict:
        """Lancer simple"""
        return self.roll(faces, NormalRoll())
    
    def roll_advantage(self, faces: int) -> dict:
        """Lancer avec avantage"""
        return self.roll(faces, AdvantageRoll())
    
    def roll_disadvantage(self, faces: int) -> dict:
        """Lancer avec désavantage"""
        return self.roll(faces, DisadvantageRoll())
    
    
if __name__ == "__main__":
    roller = DiceRoller()
    print(roller.roll_normal(6))
    print(roller.roll_advantage(20))
    print(roller.roll_disadvantage(10))