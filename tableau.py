class Tableau:
    def __init__(self, deck):
        self.piles = []

        for i in range(7):
            self.piles.append(deck.getCards(i+1))
            self.piles[i][-1].flip()

    def is_valid_move(self, destination_pile_number, card):
        if not card.is_face_up():
            return False

        first_card_destination = self.piles[destination_pile_number][-1]

        if first_card_destination.get_color() == card.get_color():
            return False

        if first_card_destination.get_rank() != card.get_rank() + 1:
            return False

        return True

    def move_pile_to_pile(self, source_pile_number, destination_pile_number,
                          card):
        if self.is_valid_move(source_pile_number, card):
            source_pile = self.piles[source_pile_number]
            destination_pile = self.piles[destination_pile_number]

            for i in range(len(source_pile)):
                if source_pile[i] == card:
                    for j in range(i, len(source_pile)):
                        destination_pile.append(source_pile.pop())
                    break

    def is_card_on_top(self, pile_number, card):
        return self.piles[pile_number][-1] == card

    def remove_card_on_top(self, pile_number, card):
        self.piles[pile_number].pop()