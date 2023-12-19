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

    def is_valid_move(self, pile_number, card):
        if self.piles[pile_number] == []:
            return card.get_rank() == 1

        first_card_destination = self.piles[pile_number][-1]

        if first_card_destination.get_suit() != card.get_suit():
            return False

        if first_card_destination.get_rank() != card.get_rank() - 1:
            return False

        return True
