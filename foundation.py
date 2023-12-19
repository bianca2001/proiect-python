#A kind of pile. 
# The goal of many solitaire games is to eventually move all the cards onto the foundation piles. 
# Usually the foundations are empty at the start of a game, but in some games they may begin with 
# a starter card.

class Foundation:
    def __init__(self, suit):
        self.piles = []

    def add_card(self, pile_number, card):
        self.piles[pile_number].append(card)

    def get_top_card(self, pile_number):
        return self.piles[pile_number][-1]
