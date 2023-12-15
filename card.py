class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def is_red(self):
        return self.suit in ["Hearts", "Diamonds"]

    def is_black(self):
        return self.suit in ["Spades", "Clubs"]