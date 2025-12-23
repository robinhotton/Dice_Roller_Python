class DiceValidator:
    """Valide les paramètres de lancer de dés"""
    
    STANDARD_DICE = [4, 6, 8, 10, 12, 20, 100]
    
    @classmethod
    def is_valid_die(cls, faces: int) -> bool:
        """Vérifie si le dé est standard"""
        return faces in cls.STANDARD_DICE
    
    @classmethod
    def validate_die(cls, faces: int) -> None:
        """Lève une exception si le dé n'est pas valide"""
        if not cls.is_valid_die(faces):
            raise ValueError(
                f"Dé d{faces} non supporté. "
                f"Dés autorisés : {cls.STANDARD_DICE}"
            )
    
    @classmethod
    def validate_count(cls, count: int) -> None:
        """Valide un nombre de dés"""
        if not isinstance(count, int) or count < 1:
            raise ValueError("Le nombre doit être un entier >= 1")