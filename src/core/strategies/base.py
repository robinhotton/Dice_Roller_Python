from abc import ABC, abstractmethod
from ..dice import Dice

class RollStrategy(ABC):
    """Interface pour les différentes stratégies de lancer"""
    
    @abstractmethod
    def execute(self, die: Dice) -> dict:
        """Exécute la stratégie et retourne un résultat structuré"""
        pass