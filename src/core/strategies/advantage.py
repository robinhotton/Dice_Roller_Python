from .base import RollStrategy
from ..dice import Dice

class AdvantageRoll(RollStrategy):
    """Lancer avec avantage (prend le meilleur de 2)"""

    def execute(self, die: Dice) -> dict:
        rolls = die.roll_multiple(2)
        final = max(rolls)
        return {
            "strategy": "advantage",
            "rolls": rolls,
            "final_value": final
        }