class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def is_red(self):
        return self.suit in ["Hearts", "Diamonds"]

    def is_black(self):
        return self.suit in ["Spades", "Clubs"]
    
    def flip(self):
        self.face_up = not self.face_up
    
    def is_face_up(self):
        return self.face_up

    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank

    def set_suit(self, suit):
        self.suit = suit
    
    def set_rank(self, rank):
        self.rank = rank