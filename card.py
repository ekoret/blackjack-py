class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    """Class string method to return human-readable string of object"""

    def __str__(self):
        return f"{self.value}{self.suit}"
