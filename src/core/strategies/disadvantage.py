from .base import RollStrategy
from ..dice import Dice

class DisadvantageRoll(RollStrategy):
    """Lancer avec désavantage (prend le pire de 2)"""

    def execute(self, die: Dice) -> dict:
        rolls = die.roll_multiple(2)
        final = min(rolls)
        return {
            "strategy": "disadvantage",
            "rolls": rolls,
            "final_value": final
        }