class Foundation:
    def __init__(self):
        self.piles = [[], [], [], []]

    def is_game_won(self):
        for pile in self.piles:
            if len(pile) != 13:
                return False
        return True

    def add_card(self, pile_number, card):
        self.piles[pile_number].append(card)

    def get_top_card(self, pile_number):
        return self.piles[pile_number][-1]

    def is_valid_move(self, pile_number, card):
        print("piles", self.piles)
        if self.piles[pile_number] == []:
            return card.get_rank() == 1

        first_card_destination = self.piles[pile_number][-1]

        if first_card_destination.get_suit() != card.get_suit():
            return False

        if first_card_destination.get_rank() != card.get_rank() - 1:
            return False

        return True

    def remove_card(self, pile_number):
        self.piles[pile_number].pop()

    def is_full(self):
        for pile in self.piles:
            if len(pile) != 13:
                return False
        return True
