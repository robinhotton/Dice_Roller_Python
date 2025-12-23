from .base import RollStrategy
from ..dice import Dice

class NormalRoll(RollStrategy):
    """Lancer simple"""

    def execute(self, die: Dice) -> dict:
        result = die.roll()
        return {
            "strategy": "normal",
            "rolls": [result],
            "final_value": result,
        }